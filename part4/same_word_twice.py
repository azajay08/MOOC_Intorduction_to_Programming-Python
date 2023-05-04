# Write your solution here
my_list = []
i = 0
while True:
	word = input("Word: ")
	if word in my_list:
		print(f"You typed in {i} different words")
		break
	my_list.append(word)
	i += 1
