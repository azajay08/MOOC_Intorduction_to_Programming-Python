# Write your solution here
items = []
while True:
	item = int(input(f"New item: "))
	if item == 0:
		print("Bye!")
		break
	items.append(item)
	order = sorted(items)
	print(f"The list now: {items}")
	print(f"The list in order: {order}")