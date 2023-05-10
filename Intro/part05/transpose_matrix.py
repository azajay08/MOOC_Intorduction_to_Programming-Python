# Write your solution here
def transpose(matrix: list):
	for x in range(len(matrix)):
		for y in range(x, len(matrix)):
			matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]


if __name__ == "__main__":
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	transpose(matrix)
	print(matrix)