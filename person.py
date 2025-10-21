import pydot

class Person:
	id_counter = 0

	def __init__(self, name, birthday):
		self._id = Person.id_counter
		Person.id_counter += 1

		self.name = name
		self.birthday = birthday

		self.children = list()
		self.parents = list()

		self.node = pydot.Node(self.NodeName(), label=self.name)
		self.children_edges = list()


	def __str__(self):
		return f"Person({self._id}, name='{self.name}')"

	def NodeName(self):
		return str(self._id)

	def AddChild(self, person):
		if person not in self.children:
			self.children.append(person)
			edge = pydot.Edge(self.NodeName(), person.NodeName(), color="black")
			self.children_edges.append(edge)

	def AddParent(self, person):
		if person not in self.parents:
			self.parents.append(person)


	def PrintAllDescendants(self, lvl=0):
		tabs = "  " * lvl
		print(f"{tabs}*--- {self}")

		for child in self.children:
			child.PrintAllDescendants(lvl + 1)


