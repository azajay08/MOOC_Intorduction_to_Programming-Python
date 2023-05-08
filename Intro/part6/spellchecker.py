# write your solution here
sentence = input("Write text: ")
s_split = sentence.split()
spell = []
with open('wordlist.txt') as file:
	for word in file:
		spell.append(word.strip())
	for word in s_split:
		if word.lower() in spell:
			wrd = word.strip()
			print(f"{word} ", end= '')
		else:
			print(f"*{word}* ", end= '')
	print()
