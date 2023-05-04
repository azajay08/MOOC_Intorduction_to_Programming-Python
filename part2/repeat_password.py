# Write your solution here
passwd = input("Password: ")
while 1:
	repeat = input("Repeat password: ")
	if repeat == passwd:
		print("User account created!")
		break
	print("They do not match!")
	