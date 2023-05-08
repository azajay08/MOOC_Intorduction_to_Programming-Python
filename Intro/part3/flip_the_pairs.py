# Write your solution here
num = int(input("Please type in a number: "))
i = 2
if num == 1:
	print (1)
while i <= num:
	print(i)
	if i == num and num % 2:
		break
	i -= 1
	print(i)
	if i + 3 > num:
		i += 2
	else:
		i += 3