# Write your solution here

def prime_numbers():
	num = 2
	while True:
		for a in range(2, num):
			if num % a == 0:
				break
		else:
			yield num
		num += 1

if __name__ == "__main__":
	numbers = prime_numbers()
	for i in range(8):
		print(next(numbers))