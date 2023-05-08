# Write your solution here
import random

def roll(die: str):
	if die == "A":
		dice = [3, 3, 3, 3, 3, 6]
	elif die == "B":
		dice = [2, 2, 2, 5, 5, 5]
	elif die == "C":
		dice = [1, 4, 4, 4, 4, 4]
	return random.choice(dice)

def play(die1: str, die2: str, times: int):
	res1 = 0
	res2 = 0
	draw = 0
	for i in range(times):
		p1 = roll(die1)
		p2 = roll(die2)
		if p1 == p2:
			draw += 1
		elif p1 > p2:
			res1 += 1
		else:
			res2 += 1
	result = (res1, res2, draw)
	return result

if __name__ == "__main__":
	result = play("A", "C", 1000)
	print(result)
	result = play("B", "B", 1000)
	print(result)
	# for i in range(20):
	# 	print(roll("A"), " ", end="")
	# print()
	# for i in range(20):
	# 	print(roll("B"), " ", end="")
	# print()
	# for i in range(20):
	# 	print(roll("C"), " ", end="")