#!/usr/bin/env python3
import requests
import json
import argparse

parser = argparse.ArgumentParser()
args = parser.parse_args()

api_url="https://note.mu/api/v2/search_histories/"
resp = requests.get(api_url)

print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
