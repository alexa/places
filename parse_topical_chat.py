"""
Helper script to parse Topical Chat into a simpler jsonlist file.
"""

import os
import json
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--tc_path", type=str, default=None)
    return parser.parse_args()


def main():
    args = parse_args()
    with open(os.path.join(args.tc_path, "conversations/train.json"), "r") as tc_f, \
            open('prompts/all_topicalchat_train.jsonlist', 'w') as parsed_f:
        data = json.load(tc_f)
        for conversation in data:
            turns = [t['message'] for t in data[conversation]['content']]
            parsed_conversation = {
                "conversation_id": conversation,
                "conversation": turns,
                "domain": data[conversation]['article_url'].split('/')[3].capitalize()
            }

            parsed_f.write(json.dumps(parsed_conversation) + '\n')


if __name__ == "__main__":
    main()
