# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
	i = 0
	num = 1
	while num < 10:
		x = 0
		count = 0
		while x < 3:
			y = 0
			while y < 3:
				# print(sudoku[row_no + x][column_no + y])
				if sudoku[row_no + x][column_no + y] == num:
					count += 1
				y += 1
			x += 1
		num += 1
		if count > 1:
			return False
	return True

if __name__ == "__main__":
	sudoku = [
	[9, 0, 0, 0, 8, 0, 3, 0, 0],
	[2, 0, 0, 2, 5, 0, 7, 0, 0],
	[0, 2, 0, 3, 0, 0, 0, 0, 4],
	[2, 9, 4, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 7, 3, 0, 5, 6, 0],
	[7, 0, 5, 0, 6, 0, 4, 0, 0],
	[0, 0, 7, 8, 0, 3, 9, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 3],
	[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	print(block_correct(sudoku, 0, 0))
	print(block_correct(sudoku, 1, 2))