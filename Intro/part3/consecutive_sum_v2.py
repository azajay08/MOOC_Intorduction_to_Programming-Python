# Write your solution here
num = int(input("Limit: "))
i = 1
res = 0
calc = ""
while res < num:
	if i == 1:
		calc += f"{i} "
	else:
		calc += f"+ {i} "
	res += i
	i += 1
print(f"The consecutive sum: {calc} = {res}")