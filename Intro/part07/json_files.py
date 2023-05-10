# Write your solution here
import json

def print_persons(filename: str):
	with open(filename) as file:
		data = file.read()
	
	info = json.loads(data)
	for inf in info:
		hobbies = ', ' .join(inf['hobbies'])
		print(f"{inf['name']} {inf['age']} years ({hobbies})")


if __name__ == "__main__":
	print_persons("file1.json")