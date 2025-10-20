#!/usr/bin/python3

import sys
import argparse
import json

from person_registry import PersonRegistry
from person import Person


ap = argparse.ArgumentParser()
ap.add_argument('input_file', type=str, help='JSON file to parse')


args = ap.parse_args()

json_obj = None
with open(args.input_file, "r") as f:
	json_obj = json.load(f)


print("json:", json_obj["people"])
print()
print("dir(json):", dir(json_obj["people"]))


people = json_obj["people"]

registry = PersonRegistry()
for name in people.keys():
	p = registry.GetOrAddPerson(name)
	for child_name in people[name]:
		child = registry.GetOrAddPerson(child_name)
		p.AddChild(child)


print()
print()
for name in registry.people:
	print(registry.people[name])


