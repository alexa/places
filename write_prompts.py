"""
Helper script to semi-programmatically write prompts.
python write_prompts.py
"""

import os
import json
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--fits_path", type=str, default=None)
    return parser.parse_args()


def main():
    args = parse_args()
    with open(os.path.join(args.fits_path, "data/fits/human_model_chats/train.txt"), "r") as f:
        line = f.readline()
        fits_data = []

        while line:
            example = json.loads(line)
            fits_data.append(example)
            line = f.readline()

    generic_topics = set([x['generic_topic'] for x in fits_data])
    print(len(generic_topics))
    prompt_mapping = dict()

    for topic in generic_topics:
        print(topic)
        print('Your prompt: ')
        prompt = input()
        prompt_mapping[topic] = prompt
        print(prompt)

        with open('prompts/fits_generic_topic_prompt_mapping.json', 'w') as f:
            json.dump(prompt_mapping, f)


if __name__ == "__main__":
    main()
