# Write your solution here
while True:
	print("1 - Add word, 2 - Search, 3 - Quit")
	cmd = int(input("Function: "))
	if cmd == 1:
		with open("dictionary.txt", "a") as file:
			f_word = input("The word in Finnish")
			e_word = input("The word in English")
			file.write(f"{f_word} - {e_word}")
			file.close()
			print("Dictionary entry added")
	elif cmd == 2:
		with open("dictionary.txt", "r") as file:
			s_word = input("Search term: ")
			for line in file:
				if s_word in line:
					print(line)
			file.close()
	else:
		print("Bye!")
		break