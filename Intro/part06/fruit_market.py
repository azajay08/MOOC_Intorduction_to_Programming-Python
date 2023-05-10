# write your solution here
def read_fruits():
	with open("fruits.csv") as file:
		fruits = {}
		for line in file:
			l_split = line.strip().split(";")
			fruits[l_split[0]] = float(l_split[1])
	return fruits

if __name__ == "__main__":
	fruits = read_fruits()