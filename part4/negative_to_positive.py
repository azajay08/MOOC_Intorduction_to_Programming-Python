# Write your solution here
num = int(input("Please type in a positive integer: "))
neg = num * -1
for i in range(neg, num + 1):
	if i == 0:
		continue
	print(i)