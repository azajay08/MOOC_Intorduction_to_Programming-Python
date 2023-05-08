# Write your solution here
import string


def separate_characters(my_string: str):
	str1 = ''
	str2 = ''
	str3 = ''
	for i in my_string:
		if i in string.ascii_letters:
			str1 += i
		elif i in string.punctuation:
			str2 += i
		else:
			str3 += i

	str_tup = (str1, str2, str3)
	return str_tup

if __name__ == "__main__":
	parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
	print(parts[0])
	print(parts[1])
	print(parts[2])