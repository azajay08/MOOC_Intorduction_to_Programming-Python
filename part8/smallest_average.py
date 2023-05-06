# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
	av1 = 0
	av2 = 0
	av3 = 0
	for k in person1.values():
		try:
			av1 += int(k)
		except ValueError:
			pass
	for k in person2.values():
		try:
			av2 += int(k)
		except ValueError:
			pass
	for k in person3.values():
		try:
			av3 += int(k)
		except ValueError:
			pass
	if min(av1, av2, av3) == av1:
		return person1
	elif min(av1, av2, av3) == av2:
		return person2
	else:
		return person3



if __name__ == "__main__":
	person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
	person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
	person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

	print(smallest_average(person1, person2, person3))