# Write your solution here
def chessboard(num):
	i = 1
	x = 1
	row = 0
	while row < num:
		count = 0
		i = x
		while count < num:
			print(f"{i}", end= '')
			if i == 0:
				i = 1
			else:
				i = 0
			count += 1
		row += 1
		print()
		if x == 0:
			x = 1
		else:
			x = 0
# Testing the function
if __name__ == "__main__":
    chessboard(4)
