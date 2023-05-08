# write your solution here
def row_sums():
	with open("matrix.txt") as file:
		sum_list = []
		num_sum = 0
		for line in file:
			l_split = line.strip().split(",")
			num_sum = 0
			for num in l_split:
				num_sum += int(num)
			sum_list.append(num_sum)
			# sum_list.append(sum(l_split))
	return sum_list

def matrix_max():
	with open("matrix.txt") as file:
		numbers = []
		for line in file:
			l_split = line.strip().split(",")
			for num in l_split:
				numbers.append(int(num))
	return max(numbers)

def matrix_sum():
	with open("matrix.txt") as file:
		msum = 0
		for line in file:
			l_split = line.strip().split(",")
			for num in l_split:
				msum += int(num)
		return msum

if __name__ == "__main__":
	with open("matrix.txt") as file:
		print(matrix_sum())
		print(matrix_max())
		print(row_sums())