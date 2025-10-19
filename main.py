#!/usr/bin/python3

import sys
import argparse




ap = argparse.ArgumentParser()
ap.add_argument('input_file', type=str, help='JSON file to parse')


args = ap.parse_args()


print("Do this file:", args.input_file)

