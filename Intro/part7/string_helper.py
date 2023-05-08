# Write your solution here

def change_case(orig_string: str):
	new_str = ""
	for i in orig_string:
		new_str += i.swapcase()
	return new_str

def split_in_half(orig_string: str):
	half = len(orig_string) // 2
	first = orig_string[:half]
	second = orig_string[half:]

	return(first, second)

def remove_special_characters(orig_string: str):
	new_str = ""
	for i in orig_string:
		if not i.isalnum() and not i.isspace():
			continue
		else:
			new_str += i
	return new_str