# Write your solution here
def same_chars(str1, n1, n2):
	if n1 < len(str1) and n2 < len(str1):
		if str1[n1] == str1[n2]:
			return True
		else:
			return False
	else:
		return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))