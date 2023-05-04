# Write your solution here
def calculate_sum(calc, answer):
	if "-" in calc:
		m_split = calc.split('-')
		if int(m_split[0]) - int(m_split[1]) == answer:
			return 1
		return 0
	elif "+" in calc:
		m_split = calc.split('+')
		if int(m_split[0]) + int(m_split[1]) == answer:
			return 1
		return 0

def filter_solutions():
	with open("solutions.csv") as file:
		open('correct.csv', 'w').close()
		with open("correct.csv", "a") as c_file:
			open('incorrect.csv', 'w').close()
			with open("incorrect.csv", "a") as i_file:
				for line in file:
					l_split = line.strip().split(";")
					if calculate_sum(l_split[1], int(l_split[2])):
							c_file.write(line)
					else:
							i_file.write(line)
					
		c_file.close()
		i_file.close()


if __name__ == "__main__":
	filter_solutions()