# Write your solution here
def longest_series_of_neighbours(my_list):
	best = 0
	i = 0
	l_len = len(my_list) - 1
	while i < l_len:
		count = 1
		while (my_list[i] - my_list[i + 1] == 1) or (my_list[i + 1] - my_list[i] == 1):
			count += 1
			i += 1
			if i == l_len:
				break
		if count > best:
			best = count
		i += 1
	return best


if __name__ == "__main__":
	my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
	print(longest_series_of_neighbours(my_list))