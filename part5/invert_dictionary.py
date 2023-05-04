# Write your solution here
def invert(dictionary):
	new_dictionary = {val: key for key, val in dictionary.items()}
	dictionary.clear()
	dictionary.update(new_dictionary)

if __name__ == "__main__":
	s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
	invert(s)
	print(s)