# Write your solution here

def distinct_numbers(my_list):
	new_list = []
	for i in sorted(my_list):
		if i not in new_list:
			new_list.append(i)

	return new_list

if __name__ == "__main__":
	my_list = [3, 2, 2, 1, 3, 3, 1]
	print(distinct_numbers(my_list)) # [1, 2, 3]