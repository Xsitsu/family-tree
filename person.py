class Person:
	def __init__(self, name, birthday):
		self.name = name
		self.birthday = birthday

	def __str__(self):
		return f"Person(name={self.name}, birthday={self.birthday})"

