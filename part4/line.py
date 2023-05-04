# Write your solution here
def line(num, str1):
	if str1:
		print(str1[0] * num)
	else:
		print("*" * num)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(3, "")