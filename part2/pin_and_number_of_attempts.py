# Write your solution here
i = 1
while 1:
	pin = int(input("PIN: "))
	if pin == 4321:
		break
	i += 1
	print("Wrong")
if i == 1:
		print("Correct! It only took you one single attempt!")
else:
	print(f"Correct! It took you {i} attempts")