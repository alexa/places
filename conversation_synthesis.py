"""
This script generates an entire synthetic conversational dataset.
python synthetic_convo_gen.py --model opt30b --examples first_three --use_detailed_prompt 

Detailed/un-detailed prompt, add --use_detailed_prompt
Un-detailed prompt: Alice is interested in <generic topic>.
Detailed prompt: Alice studied X in college. Bob wants to learn more about X.

Random sample topics to generate for:
--random_sample 200 to generate 200 dialogues

--in_context_dataset: Choose the dataset to load in-context examples from:
           "fits" - FITS
           "daily_dialog" - Daily Dialog
           "topical_chat" - Topical Chat

--in_context_dataset_path: Path to the chosen dataset for in-context examples
--fits_path: Path to the FITS dataset
"""

import math
from argparse import ArgumentParser
import os
from utils import fits_domain_renaming, swap_words, \
    triadic_conversation_pool, dyda_topic_map
from utils import conversation_pool as NormalConversationPool
from load_models import load_opt30b, load_gptj, load_opt13b, load_opt66b, load_gptneo20b
import json
import time
import random
from datasets import load_dataset


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--model", type=str, default="gptj",
                        choices=["gptj", "gpt-neox-20b", "opt30b", "opt66b", "opt13b"])
    parser.add_argument("--examples", type=str, default="first_three",
                        choices=['first_three', 'random'])
    parser.add_argument("--use_detailed_prompt", action='store_true', default=False)
    parser.add_argument("--randomize_names", action='store_true', default=False)
    parser.add_argument("--triadic", action='store_true', default=False)
    parser.add_argument("--random_sample", type=int, default=None)
    parser.add_argument("--num_in_context_examples", type=int, default=3)
    parser.add_argument("--in_context_dataset", type=str, default="fits",
                        choices=["fits", "daily_dialog", "topical_chat"])
    parser.add_argument("--in_context_dataset_path", type=str, default=None)
    parser.add_argument("--fits_path", type=str, default=None)
    return parser.parse_args()


def main():
    args = parse_args()    
    if args.triadic:
        print("Triadic conversations")
        conversation_pool = triadic_conversation_pool

        with open("prompts/triadic_fits_generic_topic_prompt_mapping.json", "r") as f:
            generic_topic_prompt_map = json.load(f)
    else:
        if args.in_context_dataset == 'daily_dialog':
            dyda_topics = []
            with open(os.path.join(args.in_context_dataset_path, "dialogues_topic.txt"), "r") as f:
                line = f.readline()
                while line:
                    topic = line
                    dyda_topics.append(topic)
                    line = f.readline()

            conversation_pool = []
            ex = load_dataset("daily_dialog")
            train_dialogs = ex['train']['dialog']

            for dialognum, dialog in enumerate(train_dialogs):
                conv_str = "The following is a conversation between two speakers about {}.".format(
                    dyda_topic_map[int(dyda_topics[dialognum].rstrip())]
                )

                for i, utt in enumerate(dialog):
                    if i % 2 == 0:
                        speaker = "Speaker 1"
                    else:
                        speaker = "Speaker 2"

                    conv_str = conv_str + "\n{}: {}".format(speaker, utt)
                conversation_pool.append(conv_str)
            print("Created DailyDialog Conversation Pool")

        elif args.in_context_dataset == 'topical_chat':
            conversation_pool = []

            with open("prompts/all_topicalchat_train.jsonlist", "r") as f:
                line = f.readline()

                while line:
                    convo = json.loads(line)
                    domain = convo['domain']
                    conv_str = "The following is a conversation between two speakers about {}.".format(domain)

                    for i, utt in enumerate(convo['conversation']):
                        if i % 2 == 0:
                            speaker = "Speaker 1"

                        else:
                            speaker = "Speaker 2"

                        conv_str = conv_str + "\n{}: {}".format(speaker, utt)
                    conversation_pool.append(conv_str)                    
                    line = f.readline()
            print("Created Topical-Chat Conversation Pool")

        elif args.in_context_dataset == 'fits':
            conversation_pool = NormalConversationPool

        with open("prompts/fits_generic_topic_prompt_mapping.json", "r") as f:
            generic_topic_prompt_map = json.load(f)

    with open(os.path.join(args.fits_path, "data/fits/human_model_chats/train.txt"), "r") as f:
        line = f.readline()
        fits_data = []

        while line:
            example = json.loads(line)
            fits_data.append(example)
            line = f.readline()

    fits_indices = [i for i in range(len(fits_data))]

    if args.random_sample:
        fits_indices = random.sample(fits_indices, args.random_sample)

    output_file_name = "{}_{}generated_conversations_using_{}_examples{}{}{}{}{}.jsonlist".format(
        args.model,
        "triadic_" if args.triadic else "",
        args.examples,
        "_with_detailed_prompt" if args.use_detailed_prompt else "",
        "_with_randomized_speakers" if args.randomize_names else "",
        "_{}_randomly_sampled".format(args.random_sample) if args.random_sample else "",
        "_{}_in_context_examples".format(args.num_in_context_examples) if args.num_in_context_examples != 3 else "",
        args.in_context_dataset
        )
    conversations_written = 0

    if os.path.exists(output_file_name):
        with open(output_file_name, 'r') as f:
            line = f.readline()
            while line:
                conversations_written += 1
                line = f.readline()

        print("Read {} existing dialogs".format(conversations_written))

    if args.model == "gptj":
        model_loader = load_gptj
    elif args.model == "opt30b":
        model_loader = load_opt30b
    elif args.model == "opt66b":
        model_loader = load_opt66b
    elif args.model == "opt13b":
        model_loader = load_opt13b
    elif args.model == "gpt-neox-20b":
        model_loader = load_gptneo20b
    else:
        raise NotImplementedError

    model, tokenizer = model_loader()
    overall_start = time.time()
    if args.random_sample:
        conversation_indices = fits_indices
        total_conversations = len(conversation_indices)
    else:
        total_conversations = len(fits_data)
        conversation_indices = list(range(conversations_written, total_conversations))

    for fits_index in conversation_indices:
        fits_topics = fits_data[fits_index]

        if args.examples == "first_three":
            examples_idx = [0, 1, 2]
            examples = conversation_pool[:3]

        else:
            examples_idx = random.sample([i for i in range(len(conversation_pool))], args.num_in_context_examples)
            examples = [conversation_pool[i] for i in examples_idx]

        generic_topic = fits_topics['generic_topic']
        domain = fits_domain_renaming[fits_topics['domain']].lower()
        prompt = "" 
        for i, example in enumerate(examples):
            prompt = prompt + "<Conversation {}>\n{}\n".format(i, example)
        prompt = prompt + "<Conversation {}>\n".format(len(examples))

        if args.triadic:
            prompt = \
                prompt + "The following is a conversation between Alice and Bob and Claire about {}. ".format(domain)
        else:
            if args.in_context_dataset in ['daily_dialog', 'topical_chat']:
                prompt = prompt + "The following is a conversation between two speakers about {}. ".format(domain)
            else:
                prompt = prompt + "The following is a conversation between Alice and Bob about {}. ".format(domain)

        if args.use_detailed_prompt:
            prompt_personality = generic_topic_prompt_map[generic_topic].rstrip().lstrip()
        else:
            prompt_personality = "Alice is interested in {}.".format(generic_topic.lower().rstrip().lstrip())
        
        if args.randomize_names:
            prompt_personality = prompt_personality.replace(" he ", " they ")
            prompt_personality = prompt_personality.replace("He ", "they ")
            prompt_personality = prompt_personality.replace(" she ", " they ")
            prompt_personality = prompt_personality.replace("She ", "they ")
            prompt_personality = prompt_personality.replace(" his ", " their ")
            prompt_personality = prompt_personality.replace("His ", "their ")
            prompt_personality = prompt_personality.replace(" her ", " their ")
            prompt_personality = prompt_personality.replace("Her ", "Their ")

            if ("Alice" in prompt_personality and "Bob" not in prompt_personality) or \
                    ("Bob" in prompt_personality and "Alice" not in prompt_personality):
                # If only one of Bob and Alice are present, with 50% probability set the speaker to be Alice or Bob.
                # The original distribution was Alice/Bob in the sole speaker case is biased towards Alice.
                if random.random() >= 0.50:
                    speaker1 = "Bob"
                    speaker2 = "Alice"
                else:
                    speaker1 = "Alice"
                    speaker2 = "Bob"
                prompt_personality = prompt_personality.replace("Alice", speaker1)
                prompt_personality = prompt_personality.replace("Bob", speaker2)

            else:
                # There is always at least one speaker, so in this case Alice and Bob are both present in the prompt.
                # The ordering of Alice/Bob is not set with 50% probability originally.
                # Here, we just randomly swap whatever is the existing ordering with 50% probability.
                if random.random() >= 0.50:
                    prompt_personality = swap_words(prompt_personality, "Alice", "Bob")

        prompt = prompt + prompt_personality + "\n" "Alice:"

        if args.in_context_dataset in ['daily_dialog', 'topical_chat']:
            prompt = prompt.replace("Alice", "Speaker 1")
            prompt = prompt.replace("Bob", "Speaker 2")

        start = time.time()
    
        print("PROMPT")
        print(prompt)

        encoded_inputs = tokenizer(prompt, return_tensors='pt')
        input_ids = encoded_inputs.input_ids
        input_ids = input_ids.to("cuda")
        attention_mask = encoded_inputs.attention_mask.to("cuda")
        gen_length = min(math.ceil(len(input_ids[0]) * 1.5), 2048)

        if gen_length < 256:
            gen_length = 256

        gen_tokens = model.generate(
            input_ids,
            attention_mask=attention_mask,
            do_sample=True,
            top_p=0.92, 
            top_k=0,
            num_return_sequences=1,
            max_length=gen_length,
        )

        gen_text = tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)   
        end = time.time()
        print("PROMPT")
        print(prompt)
        print("----------")

        for instance in gen_text:
            print(instance)
            print("----------")
            parsing = instance.split("<Conversation {}>".format(len(examples)))[1].split("\n")[2:]
            i = 0
            dialog = []
            print("PARSED RESULT")

            while i < len(parsing) and ':' in parsing[i]:
                parsed_sentence = parsing[i]
                dialog.append(parsed_sentence)
                print(parsed_sentence)
                i += 1

            if len(dialog) > 0:
                with open(output_file_name, 'a') as f:
                    f.write(json.dumps({
                        'conversation': dialog,
                        'domain': domain,
                        'prompt_personality': prompt_personality,
                        'in_context_examples': examples_idx,
                        'conv_id': fits_index
                    }))
                    f.write('\n')

        print("Time elapsed: {}".format(end - start))
        print("Wrote to", output_file_name)
        conversations_written += 1
        print("{} of {} total conversations written".format(conversations_written, total_conversations))
        print("Total time elapsed: {}".format(time.time() - overall_start))
        print("----------")

    quit()


if __name__ == "__main__":
    main()
