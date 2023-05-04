# Write your solution here

def length_of_longest(my_list):
	best = 0
	for i in my_list:

		if len(i) > best:
			best = len(i)
	return best

if __name__ == "__main__":
	my_list = ["first", "second", "fourth", "eleventh"]
	result = length_of_longest(my_list)
	print(result)