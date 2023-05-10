# Write your solution here
while 1:
	word = input("Please type in a string: ")
	str1 = ""
	if word == "":
		break
	i = 0
	while i < len(word):
		str1 += "-"
		i += 1
	print(word)
	print(str1)

