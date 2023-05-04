# Write your solution here
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
	

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
	print(number)
	sudoku[row_no][column_no] = number

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

	print_sudoku(sudoku)
	add_number(sudoku, 0, 0, 2)
	add_number(sudoku, 1, 2, 7)
	add_number(sudoku, 5, 7, 3)
	print()
	print("Three numbers added:")
	print()
	print_sudoku(sudoku)