# Write your solution here
def read_input(str, min, max):
	while True:
		try:
			prompt = int(input(f"{str}"))
			if prompt >= min and prompt <= max:
				return prompt
			print(f"You must type in an integer between {min} and {max}")

		except ValueError:
			print(f"You must type in an integer between {min} and {max}")

		



if __name__ == "__main__":
	number = read_input("Please type in a number: ", 5, 10)
	print("You typed in:", number)