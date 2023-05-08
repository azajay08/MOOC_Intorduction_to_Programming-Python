# Write your solution here
far = float(input("Please type in a temperature (F): "))
cel = (far - 32) / 1.8
print(f"{far} degrees Fahrenheit equals {cel} degrees Celsius")
if cel < 0.0:
	print("Brr! It's cold in here!")