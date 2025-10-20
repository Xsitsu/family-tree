from person import Person

class PersonRegistry:
	def __init__(self):
		self.people = dict()

	def __str__(self):
		return f"PersonRegistry()"


	def GetPerson(self, name):
		if name in self.people:
			return self.people[name]
		return None

	def AddPerson(self, name):
		p = Person(name, 0)
		self.people[name] = p
		return p

	def GetOrAddPerson(self, name):
		p = self.GetPerson(name)
		if p is None:
			p = self.AddPerson(name)
		return p

