# Write your solution here
c1 = input("1st letter: ")
c2 = input("2nd letter: ")
c3 = input("3rd letter: ")
if (c1 > c2 and c1 < c3) or (c1 > c3 and c1 < c2):
	middle = c1
elif (c2 > c1 and c2 < c3) or (c2 > c3 and c2 < c1):
	middle = c2
else:
	middle = c3
print(f"The letter in the middle is {middle}")