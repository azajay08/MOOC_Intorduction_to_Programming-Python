# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int):
	numbers = []
	for i in range(amount):
		num = random.randint(lower, upper)
		while num not in numbers:
			numbers.append(num)
	return sorted(numbers)

if __name__ == "__main__":
	for number in lottery_numbers(7, 1, 40):
		print(number)