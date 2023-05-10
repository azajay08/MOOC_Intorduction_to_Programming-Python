# Write your solution here
word = input("Please type in a word: ")
if len(word) % 2 == 0:
	start = 15 - (len(word) // 2) - 1
else:
	start = 15 - (len(word) // 2) - 2
end = 15 - (len(word) // 2) - 1
print("*" * 30)
print("*" + (" " * start) + word + (" " * end) + "*")
print("*" * 30)