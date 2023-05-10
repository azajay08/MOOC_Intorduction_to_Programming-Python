# Write your solution here
word = input("Please type in a string: ")
l = len(word)
i = l - 1
while i >= 0:
	print(word[i:l])
	i -= 1