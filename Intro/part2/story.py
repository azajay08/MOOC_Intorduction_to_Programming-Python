# Write your solution here
story = ""
temp = ""
while 1:
	word = input("Please type in word: ")
	if word == temp or word == "end":
		break
	temp = word
	story += word + " "
print(story)