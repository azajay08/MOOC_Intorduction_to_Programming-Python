# Write your solution here
def row_sums(my_matrix: list):
	for x in my_matrix:
		m_sum = 0
		for i in x:
			m_sum += i
		x.append(m_sum)

if __name__ == "__main__":
	my_matrix = [[1, 2,], [3, 4]]
	row_sums(my_matrix)
	print(my_matrix)