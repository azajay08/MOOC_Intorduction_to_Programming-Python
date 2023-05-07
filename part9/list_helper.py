# WRITE YOUR SOLUTION HERE:
class ListHelper:
	@classmethod
	def greatest_frequency(cls, my_list: list):
		count = 0
		num = my_list[0]
		for n in my_list:
			if my_list.count(n) > count:
				num = n
				count = my_list.count(n)
		return num

	@classmethod
	def doubles(cls, my_list: list):
		count = 0
		num = []
		for n in my_list:
			if my_list.count(n) > 1 and n not in num:
				num.append(n)
				count += 1
		return count


if __name__ == "__main__":
	numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
	print(ListHelper.greatest_frequency(numbers))
	print(ListHelper.doubles(numbers))