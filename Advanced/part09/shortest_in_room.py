# WRITE YOUR SOLUTION HERE:
class Person:
	def __init__(self, name: str, height: int):
		self.name = name
		self.height = height

	def __str__(self):
		return self.name

class Room:
	def __init__(self):
		self.people = []
		self.count = 0
		self.height = 0

	def add(self, person: Person):
		self.people.append(person)
		self.count += 1
		self.height += person.height

	def is_empty(self):
		if self.people:
			return False
		return True

	def print_contents(self):
		print(f"There are {self.count} persons in the room, and their combined height is {self.height} cm")
		for i in self.people:
			print(f"{i} ({i.height} cm)")

	def shortest(self):
		if self.people:
			shortest = self.people[0]
			height = self.people[0].height
			for i in self.people[1:]:
				if i.height < height:
					shortest = i
					height = i.height
			return shortest
		return 
	
	def remove_shortest(self):
		if self.people:
			shortest = self.people[0]
			height = self.people[0].height
			for i in self.people[1:]:
				if i.height < height:
					shortest = i
					height = i.height
			new = Person(shortest.name, shortest.height)
			self.people.remove(shortest)
			return new
		return 

if __name__ == "__main__":
	room = Room()

	room.add(Person("Lea", 183))
	room.add(Person("Kenya", 172))
	room.add(Person("Nina", 162))
	room.add(Person("Ally", 166))
	room.print_contents()

	print()

	removed = room.remove_shortest()
	print(f"Removed from room: {removed.name}")

	print()

	room.print_contents()