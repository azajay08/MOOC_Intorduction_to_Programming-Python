# Write your solution here
import difflib

sentence = input("Write text: ")
s_split = sentence.split()
spell = []
wrong = {}
with open('wordlist.txt') as file:
	for word in file:
		spell.append(word.strip())
	for word in s_split:
		if word.lower() in spell:
			# wrd = word.strip()
			print(f"{word} ", end= '')
		else:
			close_match = difflib.get_close_matches(word, spell)
			print(f"*{word}* ", end= '')
			wrong[word] = close_match
		
	print("\nSuggestions:")
	for k, v in wrong.items():
		print(k + ': ', end= '')
		print(*v, sep = ", ")
	# print()