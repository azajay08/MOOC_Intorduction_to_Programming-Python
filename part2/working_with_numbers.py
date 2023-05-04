# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
sum_res = 0
mean_res = 0
pos_num = 0
neg_num = 0
num_count = 0
while 1:
	num = int(input("Number: "))
	if num == 0:
		break
	num_count += 1
	if num < 0:
		neg_num += 1
	else:
		pos_num += 1
	sum_res += num
mean_res = sum_res / num_count
print(f"Numbers typed in {num_count}")
print(f"The sum of the numbers is {sum_res}")
print(f"The mean of the numbers is {mean_res}")
print(f"Positive numbers {pos_num}")
print(f"Negative numbers {neg_num}")