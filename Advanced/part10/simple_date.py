# WRITE YOUR SOLUTION HERE:
class SimpleDate:
	def __init__(self, day: int, month: int, year: int):
		self.__day = day
		self.__month = month
		self.__year = year

	def __str__(self):
		return f"{self.__day}.{self.__month}.{self.__year}"
	
	def __eq__(self, another):
		return (self.__day, self.__month, self.__year) == another
	
	def __ne__(self, another):
		return (self.__day, self.__month, self.__year) != another
	
	
	def __lt__(self, another: 'SimpleDate'):
		if self.__year < another.__year:
			return True
		elif self.__year == another.__year:
			if self.__month < another.__month:
				return True
			elif self.__month == another.__month:
				if self.__day < another.__day:
					return True
		return False

	def __gt__(self, another: 'SimpleDate'):
		if self.__eq__(another) == False and self.__lt__(another) == False:
			return True
		return False
	
	def __add__(self, to_add):
		days = ((self.__year - 1) * 360) + ((self.__month - 1) * 30) + self.__day
		days += to_add
		year = days // 360 + 1
		month = (days // 30) % 12 + 1
		day = days % 30
		return SimpleDate(day, month, year)
	
	def __sub__(self, another: 'SimpleDate'):
		days = ((self.__year - 1) * 360) + ((self.__month - 1) * 30) + self.__day
		a_days = ((another.__year - 1) * 360) + ((another.__month - 1) * 30) + another.__day
		return abs(days - a_days)
	
if __name__ == "__main__":
	d1 = SimpleDate(4, 10, 2020)
	d2 = SimpleDate(2, 11, 2020)
	d3 = SimpleDate(28, 12, 1985)

	print(d2-d1)
	print(d1-d2)
	print(d1-d3)