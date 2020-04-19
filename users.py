#!/usr/bin/env python3
import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--urlname', required=True)
args = parser.parse_args()

api_url="https://note.mu/api/v1/users/"
params = {'urlname':args.urlname}
resp = requests.get(api_url, params=params)

print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
