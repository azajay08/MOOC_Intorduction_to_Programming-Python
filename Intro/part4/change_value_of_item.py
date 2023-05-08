# Write your solution here
n_list = [1, 2, 3, 4, 5]
while True:
	ind = int(input("Index: "))
	if ind == -1:
		break
	val = int(input("New value: "))
	n_list[ind] = val
	print(n_list)