# Write your solution here
def no_vowels(str1):
	new_str = ""
	for letter in str1:
		if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
			continue
		else:
			new_str += letter
	return new_str

if __name__ == "__main__":
	my_string = "this is an example"
	print(no_vowels(my_string))