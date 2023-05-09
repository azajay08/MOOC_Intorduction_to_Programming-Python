# WRITE YOUR SOLUTION HERE:
import string

def remove_punctuation(word: str):
	new_str = ''
	for c in word:
		if c not in string.punctuation:
			new_str += c
	return new_str

def most_common_words(filename: str, lower_limit: int):
	with open(filename) as file:
		w_list = []
		for line in file:
			l_split = line.strip().split()
			for word in l_split:
				w_list.append(remove_punctuation(word))
		w_count = {word: w_list.count(word) for word in w_list}
		return {word: count for word, count in w_count.items() if count >= lower_limit}    

if __name__ == "__main__":
	most_common_words("comprehensions.txt", 3)