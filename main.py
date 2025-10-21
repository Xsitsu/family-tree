#!/usr/bin/python3

import sys
import argparse
import json
import pydot

from person_registry import PersonRegistry
from person import Person


ap = argparse.ArgumentParser()
ap.add_argument('input_files', type=str, nargs='+', help='JSON file(s) to parse')




graph = pydot.Dot("family_tree", graph_type="graph", bgcolor="white")
registry = PersonRegistry()

def parse_json_obj(json_obj):
	people = json_obj["people"]
	for name in people.keys():
		p = registry.GetOrAddPerson(name)
		for child_name in people[name]:
			child = registry.GetOrAddPerson(child_name)
			p.AddChild(child)
			child.AddParent(p)

def finalize_graph():
	for person in registry.people.values():
		graph.add_node(person.node)

	for person in registry.people.values():
		for edge in person.children_edges:
			graph.add_edge(edge)

	graph.write_png("family-tree.png")



args = ap.parse_args()

for file_name in args.input_files:
	with open(file_name, "r") as f:
		parse_json_obj(json.load(f))

finalize_graph()

