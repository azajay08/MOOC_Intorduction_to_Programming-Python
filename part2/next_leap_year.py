# Write your solution here
year = int(input("Year: "))
i = year + 1
while 1:
	if i % 4 == 0:
		if i % 100 == 0:
			if i % 400 == 0:
				print(f"The next leap year after {year} is {i}")
				break
		else:
			print(f"The next leap year after {year} is {i}")
			break
	i += 1
