# Write your solution here

book = {}
while True:
	option = int(input("command (1 search, 2 add, 3 quit): "))
	if option == 1:
		name = input("name: ")
		if name in book:
			for num in book[name]:
				print(num)
		else:
			print("no number")
	elif option == 2:
		name = input("name: ")
		p_num = input("number: ")
		if name in book:
			book[name].append(p_num)
		else:
			book[name] = [p_num]
		print("ok!")
	else:
		print("quitting...")
		break