# WRITE YOUR SOLUTION HERE:
class Car:
	def __init__(self):
		self.__km = 0
		self.__fuel = 0

	def fill_up(self):
		self.__fuel = 60

	def drive(self, km:int):
		if self.__fuel - km < 0:
			for i in range(km):
				if self.__fuel - i == 0:
					self.__fuel -= i
					self.__km += i
					break
		else:
			self.__fuel -= km
			self.__km += km



	def __str__(self):
		return f"Car: odometer reading {self.__km} km, petrol remaining {self.__fuel} litres"


if __name__ == "__main__":
	car = Car()
	print(car)
	car.fill_up()
	print(car)
	car.drive(20)
	print(car)
	car.drive(50)
	print(car)
	car.drive(10)
	print(car)
	car.fill_up()
	car.fill_up()
	print(car)