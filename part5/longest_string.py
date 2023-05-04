# Write your solution here
def longest(strings):
	best = 0
	str1 = ""
	for word in strings:
		if len(word) > best:
			best = len(word)
			str1 = word
	return str1


if __name__ == "__main__":
	strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
	strings1 = ['first', 'second', 'third']
	print(longest(strings))
	print(longest(strings1))