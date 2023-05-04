# Write your solution here
word = input("Please type in a string: ")
sec = 1
last = len(word) - 2
if word[sec] == word[last]:
	print(f"The second and the second to last characters are {word[sec]}")
else:
	print("The second and the second to last characters are different")