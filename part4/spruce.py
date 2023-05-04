# Write your solution here
def spruce(num):
	i = 0
	star = 1
	space = num - 1
	print("a spruce!")
	while i < num:
		print((" " * space) + ("*" * star))
		star += 2
		space -= 1
		i += 1
	space = num - 1
	print((" " * space) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
	spruce(1)