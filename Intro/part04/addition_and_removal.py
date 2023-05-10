# Write your solution here
my_list = []
i = 0
while True:
	print(f"The list is now {my_list}")
	command = input("a(d)d, (r)emove or e(x)it: ")
	if command == "d":
		i += 1
		my_list.append(i)
	elif command == "r":
		my_list.remove(i)
		i -= 1
	elif command == "x":
		print("Bye!")
		break
