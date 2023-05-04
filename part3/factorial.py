# Write your solution here
while 1:
	num = int(input("Please type in a number: "))
	if num <= 0:
		print("Thanks and bye!")
		break
	else:
		i = 1
		res = 1
		while i <= num:
			res *= i
			i += 1
		print(f"The factorial of the number {num} is {res}")