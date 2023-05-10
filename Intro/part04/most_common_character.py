# Write your solution here
def most_common_character(word):
	letter = ""
	lcount = 0
	best = 0
	for i in word:
		lcount = word.count(i)
		if lcount > best:
			best = lcount
			letter = i
	return letter

if __name__ == "__main__":
	first_string = "abcdbde"
	print(most_common_character(first_string))