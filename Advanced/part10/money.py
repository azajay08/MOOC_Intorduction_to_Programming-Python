# TEE RATKAISUSI TÄHÄN:
class Money:
	def __init__(self, euros: int, cents: int):
		self.__euros = euros
		self.__cents = cents

	# def euros(self):
	# 	return self.__euros

	# def cents(self):
	# 	return self.__cents

	def __str__(self):
		e = self.__euros
		c = self.__cents
		return f"{e}.{c:02} eur"

	def __eq__(self, another):
		return (self.__euros, self.__cents) == another
	
	def __ne__(self, another):
		return (self.__euros, self.__cents) != another
	
	def __gt__(self, another):
		return (self.__euros, self.__cents) > another
	
	def __lt__(self, another):
		return (self.__euros, self.__cents) < another
	
	def __add__(self, another):
		# The date of the new note is the current time
		e = self.__euros + another.__euros
		c = self.__cents + another.__cents
		if c >= 100:
			c -= 100
			e += 1
		new = Money(e, c)
		return new
	
	def __sub__(self, another):
		# The date of the new note is the current time
		e = self.__euros - another.__euros
		c = self.__cents - another.__cents
		if c < 0:
			c += 100
			e -= 1
		if e < 0:
			raise ValueError("a negative result is not allowed")
		new = Money(e, c)
		return new


# if __name__ == "__main__":
# 	e1 = Money(4, 5)
# 	print(e1)
# 	e1.euros = 1000
# 	print(e1)

	# e1 = Money(4, 5)
	# e2 = Money(2, 95)

	# e3 = e1 + e2
	# e4 = e1 - e2

	# print(e3)
	# print(e4)

	# e5 = e2-e1