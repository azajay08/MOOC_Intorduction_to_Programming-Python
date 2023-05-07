# Add the requested members to the class below:

class City:
	postcodes = {'Helsinki': '00100', 'Turku': '20100', 'Tampere': '33100', 'Rovaniemi': '96100', 'Oulu': '90100'}
	def __init__(self, name: str, population: int):
		self.__name = name
		self.__population = population

	@property
	def name(self):
		return self.__name

	@property
	def population(self):
		return self.__population
	

	def __str__(self):
		return f"{self.__name} ({self.__population} residents.)"

# if __name__ == "__main__":
	# hel = City("Helsinki", 500000, "00100")
	# tur = City("Turku", 100000, "20100")
	# tam = City("Tampere", 100000, "33100")
	# rov = City("Rovaniemi", 100000, "96100")
	# oul = City("Oulu", 100000, "90100")
	# hel = City("Helsinki", 500000)
	# tur = City("Turku", 100000)
	# tam = City("Tampere", 100000)
	# rov = City("Rovaniemi", 100000)
	# oul = City("Oulu", 100000)
	# City.postcodes['Helsinki'] = "00100"
	# City.postcodes['Turku'] = "20100"
	# City.postcodes['Tampere'] = "33100"
	# City.postcodes['Rovaniemi'] = "96100"
	# City.postcodes['Oulu'] = "90100"
	# print(City.postcodes)