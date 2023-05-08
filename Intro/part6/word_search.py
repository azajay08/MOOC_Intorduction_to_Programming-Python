# Write your solution here

def dot_search(w_src):
	temp = []
	with open("words.txt", "r") as file:
		all_words = file.read()
		word_split = all_words.strip().split()
		for word in word_split:
			matches = True
			if len(w_src) != len(word):
				continue
			for i in range(len(w_src)):
				if w_src[i] == '.':
					continue
				if word[i] != w_src[i]:
					matches = False
					break
			if matches:
				temp.append(word)
	return temp

def find_words(search_term: str):
	found = []
	if '.' in search_term:
		found = dot_search(search_term)
	else:
		with open("words.txt", "r") as file:
			all_words = file.read()
			word_split = all_words.strip().split()
			for word in word_split:
				if search_term[0] == "*":
					new_term = search_term[1:]
					if word.endswith(new_term):
						found.append(word)
				elif search_term[-1] == "*":
					new_term = search_term[:-1]
					if word.startswith(new_term):
						found.append(word)
				else:
					if word == search_term:
						found.append(word)
	return found

if __name__ == "__main__":
	print(find_words("*vokes"))
	print(find_words("beac*"))
	print(find_words("ca."))
	print(find_words("p..g"))