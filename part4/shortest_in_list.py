# Write your solution here

def shortest(my_list):
	small_str = ""
	small = len(my_list[0])
	for i in my_list:
		if len(i) < small:
			small = len(i)
			small_str = i
	return small_str

if __name__ == "__main__":
	my_list = ["first", "second", "fourth", "eleventh"]
	result = shortest(my_list)
	print(result)