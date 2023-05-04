# Write your solution here
def who_won(game_board: list):
	p1 = 0
	p2 = 0
	for row in game_board:
		for column in row:
			if column == 1:
				p1 += 1
			elif column == 2:
				p2 += 1
	if p1 == p2:
		return 0
	return 1 if p1 > p2 else 2


if __name__ == "__main__":
	print(who_won([[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]))