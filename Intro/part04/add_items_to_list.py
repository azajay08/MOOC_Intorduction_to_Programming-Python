# Write your solution here
items = []
count = int(input("How many items: "))
i = 1
while i <= count:
	item = int(input(f"item {i}: "))
	i += 1
	items.append(item)
print(items)