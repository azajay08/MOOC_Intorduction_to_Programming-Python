# Write your solution here
word = input("Please type in a string: ")
sub = input("Please type in a substring: ")
i = word.find(sub)
sub_len = len(sub)
if i >= 0:
	word = word[i + sub_len:]
	# print(word)
	s = word.find(sub)
	if s >= 0:
		i += (s + sub_len)
		print(f"The second occurrence of the substring is at index {i}.")
	else:
		print("The substring does not occur twice in the string.")
else:
	print("The substring does not occur twice in the string.")