# Write your solution here
def all_the_longest(my_list):
	new_list = []
	best = 0
	for i in my_list:
		if len(i) > best:
			new_list.clear()
			new_list.append(i)
			best = len(i)
		elif len(i) == best:
			new_list.append(i)
	return new_list
		

if __name__ == "__main":
	my_list = ["first", "second", "fourth", "eleventh"]

	result = all_the_longest(my_list)
	print(result) # ['eleventh']