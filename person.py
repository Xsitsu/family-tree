class Person:
	id_counter = 0

	def __init__(self, name, birthday):
		self._id = Person.id_counter
		Person.id_counter += 1

		self.name = name
		self.birthday = birthday

		self.children = list()

	def __str__(self):
		return f"Person({self._id}, name='{self.name}')"

	def AddChild(self, person):
		self.children.append(person)

