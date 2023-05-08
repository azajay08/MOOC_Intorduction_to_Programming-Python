# Write your solution here
def print_layers(layers):
	grid_size = (layers * 2) - 1
	grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
	x = 0
	limit = (grid_size // 2)
	dec = 0
	while x <= limit:
		y = 0
		while y <= grid_size - 1 - dec:
			grid[x][y + x] = chr(layers + 64 - x)
			grid[grid_size - y - x - 1][x] = chr(layers + 64 - x)
			grid[grid_size - x - 1][grid_size - y - x - 1] = chr(layers + 64 - x)
			grid[y + x][grid_size - x - 1] = chr(layers + 64 - x)
			y += 1
		dec += 2
		x += 1
	for line in grid:
		for char in line:
			print(char, end= '')
		print('')

def main():
	layers = int(input("layers: "))
	(print_layers(layers))


main()