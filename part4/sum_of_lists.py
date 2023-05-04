# Write your solution here

def list_sum(a, b):
	new_list = []
	x = 0
	for i in a:
		new_list.append(i + b[x])
		x += 1
	return new_list

if __name__ == "__main__":
	a = [1, 2, 3]
	b = [7, 8, 9]
	print(list_sum(a, b)) # [8, 10, 12]