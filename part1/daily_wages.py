# Write your solution here
wage = float(input("Hourly wage: "))
worked = int(input("Hours worked: "))
day = input("Day of the week: ")
if day == "Sunday":
	wages = (wage * 2) * worked
else:
	wages = wage * worked
print(f"Daily wages: {wages} euros")