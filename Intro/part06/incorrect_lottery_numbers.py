# Write your solution here

def filter_incorrect():
	with open("correct_numbers.csv", "w") as cfile:
		with open("lottery_numbers.csv") as lfile:
			count = 0
			for line in lfile:
				l_split = line.split(';')
				w_split = l_split[0].split()
				n_split = l_split[1].strip().split(',')
				try:
					week = int(w_split[1])
					if len(n_split) != 7:
						continue
					for num in n_split:
						correct = False
						num_int = int(num)
						if n_split.count(num) > 1:
							break
						if type(num_int) is not int:
							break
						try:
							if num_int >= 1 and num_int <= 39:
								correct = True
							else:
								correct = False
								break
						except:
							break
					if correct == True:
						cfile.write(line)
				except:
					continue
		cfile.close()
		

if __name__ == "__main__":
	filter_incorrect()
# num = 1
# word = "hello"
# if type(word) == int:
# 	print('yep')
# else:
# 	print("nooooo")