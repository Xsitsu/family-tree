#!/usr/bin/python3

import sys
import argparse
import json



ap = argparse.ArgumentParser()
ap.add_argument('input_file', type=str, help='JSON file to parse')


args = ap.parse_args()

json_obj = None
with open(args.input_file, "r") as f:
	json_obj = json.load(f)


print("json_obj:", json_obj)

