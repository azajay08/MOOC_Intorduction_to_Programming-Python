# Write your solution here
num = int(input("Please type in a number: "))
i = 1
x = 1
while i <= num:
	x = 1
	while x <= num:
		print(f"{i} x {x} =", i * x)
		x += 1
	i += 1