# write your solution here

def largest():
	with open("numbers.txt") as new_file:
		numbers = []
		for line in new_file:
			numbers.append(int(line))
		return max(numbers)

if __name__ == "__main__":
	print(largest())
