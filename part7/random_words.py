# Write your solution here
import random

def words(n: int, beginning: str):
	with open("words.txt") as file:
		words = []
		for line in file:
			if line.strip().startswith(beginning):
				words.append(line.strip())
		if len(words) < n:
			raise ValueError(f"There are not enough words with the beginning {beginning}")
		return random.sample(words, n)

if __name__ == "__main__":
	word_list = words(3, "ca")
	for word in word_list:
		print(word)