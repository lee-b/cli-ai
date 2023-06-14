import argparse
import requests
import sys


def run(host, prompt):
    URI = f'http://{host}/api/v1/generate'

    request = {
        'prompt': prompt,
        'max_new_tokens': 250,
        'do_sample': True,
        'temperature': 0,
        'top_p': 0.1,
        'typical_p': 1,
        'repetition_penalty': 1.18,
        'top_k': 40,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'skip_special_tokens': True,
        'stopping_strings': ['Human:', '###', 'Assistant:']
    }

    response = requests.post(URI, json=request)

    if response.status_code == 200:
        result = response.json()['results'][0]['text']
        split_result = result.split("###")[0].strip()

        print(split_result)

        return True

    else:
        print(response.result, file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")

    HOST = 'localhost:5000'

    args = parser.parse_args(sys.argv[1:])

    full_prompt = f"You are an intelligent linux command line tool, designed for use at the terminal both for three modes: chatting, outputting useful information, and for working within unix pipelines. Modes should be selected automatically from the user's instructions.  Output the most useful and appropriate response likely for the following instruction:\n\n### Human: {args.prompt}\n\n### Assistant: "

    if run(HOST, full_prompt):
        return 0
    else:
        return 1

