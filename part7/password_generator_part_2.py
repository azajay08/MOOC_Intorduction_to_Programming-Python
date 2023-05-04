# Write your solution here
import random

def generate_strong_password(lim, nb, spl):
	passwd = ""
	special = "!?=+-()#"
	passwd += chr(random.randint(97, 122))
	if nb:
		passwd += chr(random.randint(48, 57))
	if spl:
		passwd += special[(random.randint(0, 7))]
	for i in range(lim - len(passwd)):
		num = random.randint(1, 3)
		if nb and num == 1:
			passwd += chr(random.randint(48, 57))
		elif spl and num == 2:
			passwd += special[(random.randint(0, 7))]
		else:
			passwd += chr(random.randint(97, 122))
	return passwd

if __name__ == "__main__":
	for i in range(10):
		print(generate_strong_password(8, True, True))