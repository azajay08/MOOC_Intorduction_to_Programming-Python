# Copy here code of line function from previous exercise and use it in your solution
def line(num, str1):
	if str1:
		print(str1[0] * num)
	else:
		print("*" * num)

def triangle(size, c1):
	i = 1
	while i <= size:
		line(i, c1)
		i += 1
def shape(width, c1, height, c2):
	i = 0
	triangle(width, c1)
	while i < height:
		line(width, c2)
		i += 1

	
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")