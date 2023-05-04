# Write your solution here
width = int(input("Width: "))
ht = int(input("Height: "))
i = 0
str1 = ""
while i < width:
	str1 += "#"
	i += 1
i = 0
while i < ht:
	print(str1)
	i += 1