# Write your solution here
word = input("Please type in a word: ")
let = input("Please type in a character: ")
l = len(word)
i = word.find(let)
while i >= 0 and (l - i) >= 3:
	print(word[i:i + 3])
	i += 1
	word = word[i:]
	l = len(word)
	i = word.find(let)