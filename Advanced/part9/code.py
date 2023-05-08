class Item:
	def __init__(self, name: str, weight: int):
		self.__name = name
		self.__weight = weight

	def name(self):
		return self.__name
	
	def weight(self):
		return self.__weight

	def __str__(self):
		return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
	def __init__(self, maxw: int):
		self.maxw = maxw
		self.items = []
		self.iweight = 0
		self.count = 0

	def weight(self):
		return self.iweight

	def add_item(self, item: Item):
		self.items.append(item)
		if (self.iweight + item.weight()) <= self.maxw:
			self.iweight += item.weight()
			self.count += 1

	def print_items(self):
		for i in self.items:
			print(i)

	def heaviest_item(self):
		heavy = 0
		if self.items:
			for i in self.items:
				# print(i.weight())
				if i.weight() > heavy:
					heavy = i.weight()
					new = i
			return new
		return

	def __str__(self):
		if self.count == 1:
			return f"{self.count} item ({self.iweight} kg)"
		return f"{self.count} items ({self.iweight} kg)"

class CargoHold:
	def __init__(self, maxw: int):
		self.cases = []
		self.maxw = maxw
		self.count = 0
		self

	def add_suitcase(self, sc: Suitcase):
		if self.maxw - sc.iweight >= 0:
			self.maxw -= sc.iweight
			self.count += 1
			self.cases.append(sc)

	def print_items(self):
		for s in self.cases:
			s.print_items()

	def __str__(self):
		if self.count == 1:
			return f"{self.count} suitcase, space for {self.maxw} kg"
		return f"{self.count} suitcases, space for {self.maxw} kg"

if __name__ == "__main__":
	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)

	adas_suitcase = Suitcase(10)
	adas_suitcase.add_item(book)
	adas_suitcase.add_item(phone)

	peters_suitcase = Suitcase(10)
	peters_suitcase.add_item(brick)

	cargo_hold = CargoHold(1000)
	cargo_hold.add_suitcase(adas_suitcase)
	cargo_hold.add_suitcase(peters_suitcase)

	print("The suitcases in the cargo hold contain the following items:")
	cargo_hold.print_items()
