# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
	new_grid = []
	new_line = []
	for line in sudoku:
		new_line = line.copy()
		new_grid.append(new_line)
	new_grid[row_no][column_no] = number
	return new_grid

def print_sudoku(sudoku: list):
	s_line = ""
	row = 0
	for line in sudoku:
		i = 0
		while i < 9:
			if line[i] == 0:
				s_line += '_'
			else:
				s_line += str(line[i])
			i += 1
			if i % 3 == 0:
				s_line += ' '
			s_line += ' '
		s_line += '\n'
		row += 1
		if row % 3 == 0 and row < 9:
			s_line += '\n'
	print(s_line)

if __name__ == "__main__":
	sudoku  = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0]
	]

	grid_copy = copy_and_add(sudoku, 0, 0, 2)
	print("Original:")
	print_sudoku(sudoku)
	print()
	print("Copy:")
	print_sudoku(grid_copy)