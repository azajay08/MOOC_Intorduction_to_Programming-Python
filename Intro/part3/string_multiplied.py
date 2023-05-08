# Write your solution here
str1 = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))
i = 0
str2 = ""
while i < amount:
	str2 += str1
	i += 1
print(str2)