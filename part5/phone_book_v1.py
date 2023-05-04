# Write your solution here
book = {}
while True:
	option = int(input("command (1 search, 2 add, 3 quit): "))
	if option == 1:
		name = input("name: ")
		if name in book:
			print(book[name])
		else:
			print("no number")
	elif option == 2:
		name = input("name: ")
		book[name] = input("number: ")
		print("ok!")
	else:
		print("quitting...")
		break
