# Write your solution here!
class NumberStats:
	def __init__(self):
		self.numbers = 0
		self.count = 0
	
	def add_number(self, number:int):
		self.count += 1
		self.numbers += number

	def count_numbers(self):
		return self.count

	def get_sum(self):
		if self.numbers == 0:
			return 0
		return self.numbers
	
	def average(self):
		if self.numbers == 0:
			return 0
		return self.numbers / self.count
		
def main():
	stats = NumberStats()
	even = NumberStats()
	odds = NumberStats()
	print("Please type in integer numbers:")
	while True:
		num = int(input())
		if num == -1:
			break
		if num % 2 == 0:
			even.add_number(num)
		else:
			odds.add_number(num)
		stats.add_number(num)
	print("Sum of numbers:", stats.get_sum())
	print("Mean of numbers:", stats.average())
	print("Sum of even numbers:", even.get_sum())
	print("Sum of odd numbers:", odds.get_sum())

main()