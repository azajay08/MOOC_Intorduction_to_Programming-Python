# Write your solution here
def palindromes(word):
	if word == word[::-1]:
		return True
	else:
		return False

while True:
	word = input("Please type in a palindrome: ")
	if palindromes(word) == False:
		print("that wasn't a palindrome")
	else:
		print(f"{word} is a palindrome!")
		break
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# 	main()
