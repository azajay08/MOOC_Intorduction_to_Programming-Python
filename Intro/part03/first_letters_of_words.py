# Write your solution here
words = input("Please type in a sentence: ")
i = 0
while i < len(words):
	print(words[i])
	while i < len(words) and words[i] != ' ':
		i += 1
	i += 1