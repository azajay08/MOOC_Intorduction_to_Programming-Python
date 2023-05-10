# Write your solution here
def squared(str1, num):
	x = 0
	y = 0
	row = 0
	w_len = len(str1)
	i = 0
	while row < num:
		x = 0
		while x < num:
			print(f"{str1[i]}", end= '')
			i += 1
			if i == w_len:
				i = 0
			x += 1
		row += 1
		print()

if __name__ == "__main__":
	squared("ab", 5)