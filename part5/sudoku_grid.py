# Write your solution here

def row_correct(sudoku: list, row_no: int):
	num = 1
	for i in sudoku[row_no]:
		if i > 0 and sudoku[row_no].count(i) > 1:
			return False
	return True 

def column_correct(sudoku: list, column_no: int):
	i = 0
	num = 1
	while i < 9:
		count = 0
		for row in sudoku:
			if row[column_no] == num:
				count += 1
			if count > 1:
				return False
		i += 1
		num += 1
	return True

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

def sudoku_grid_correct(sudoku: list):
	# i = 0
	row = 0
	col = 0
	# while i < 9:
	while row < 9:
		col = 0
		if not row_correct(sudoku, row):
			return False
		while col < 9:
			if not column_correct(sudoku, col):
				return False
			if row % 3 == 0 and col % 3 == 0:
				if not block_correct(sudoku, row, col):
					return False
			col += 1
		row += 1
	return True
		# i += 1

if __name__ == "__main__":
	sudoku1 = [
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
	print(sudoku_grid_correct(sudoku1))
	sudoku2 = [
	[2, 6, 7, 8, 3, 9, 5, 0, 4],
	[9, 0, 3, 5, 1, 0, 6, 0, 0],
	[0, 5, 1, 6, 0, 0, 8, 3, 9],
	[5, 1, 9, 0, 4, 6, 3, 2, 8],
	[8, 0, 2, 1, 0, 5, 7, 0, 6],
	[6, 7, 4, 3, 2, 0, 0, 0, 5],
	[0, 0, 0, 4, 5, 7, 2, 6, 3],
	[3, 2, 0, 0, 8, 0, 0, 5, 7],
	[7, 4, 5, 0, 0, 3, 9, 0, 1]
	]
	print(sudoku_grid_correct(sudoku2))