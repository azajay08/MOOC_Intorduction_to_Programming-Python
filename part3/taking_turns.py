# Write your solution here
num = int(input("Please type in a number: "))
i = 1
if num == 1:
	print (1)
while i < num:
	print(i)
	print(num)
	i += 1
	num -= 1
	if i == num:
		print(i)
		break
	# print(i)
	# if i + 3 > num:
	# 	i += 2
	# else:
	# 	i += 3