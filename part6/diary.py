# Write your solution here
while True:
	print("1 - add an entry, 2 - read entries, 0 - quit")
	command = int(input("Function: "))
	if command == 0:
		print("Bye now!")
		break
	elif command == 1:
		with open('diary.txt', "a") as file:
			message = input("Diary entry: ")
			file.write(message + '\n')
			print('Diary saved')
			file.close()
	else:
		with open('diary.txt', "r") as file:
			print(file.read())
