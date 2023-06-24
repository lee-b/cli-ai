import argparse
import json
import os
import sys

import requests


def run(host, prompt, config):
    URI = f'http://{host}/api/v1/generate'

    request = {
        'prompt': prompt,
    }

    response = requests.post(URI, json=request)

    if response.status_code == 200:
        result = response.json()['results'][0]['text']
        split_result = result.split("###")[0].strip()

        print(split_result)

        return True

    else:
        print(f"ERROR: {response!r}", file=sys.stderr)
        return False


def load_config(config_file_path):
    default_config = {
        'host': 'localhost',
        'port': 5000,
    }

    try:
        local_config = json.loads(open(os.path.expanduser(config_file_path)).read())
    except FileNotFoundError:
        local_config = {}

    config = {}
    config.update(default_config)
    config.update(local_config)

    return config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")
    parser.add_argument("--config-file", "-c", default="~/.config/cli-ai/config.json")

    args = parser.parse_args(sys.argv[1:])

    config = load_config(args.config_file)

    host = f"{config['host']}:{config['port']}"
    full_prompt = f"You are an intelligent linux command line tool, designed for use at the terminal both for three modes: chatting, outputting useful information, and for working within unix pipelines. Modes should be selected automatically from the user's instructions.  Output the most useful and appropriate response likely for the following instruction:\n\n### Human: {args.prompt}\n\n### Assistant: "

    if run(host, full_prompt, config):
        return 0
    else:
        return 1

