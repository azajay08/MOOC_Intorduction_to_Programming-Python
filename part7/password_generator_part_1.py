# Write your solution here
import random

def generate_password(lim):
	passwd = ""
	for i in range(lim):
		passwd += chr(random.randint(97, 122))
	return passwd

if __name__ == "__main__":
	for i in range(10):
		print(generate_password(8))