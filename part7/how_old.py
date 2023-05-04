# Write your solution here

from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year:"))
millen = datetime(1999, 12, 31)
date = datetime(year, month, day)
diff = (millen - date).days
if diff < 0:
	print("You weren't born yet on the eve of the new millennium.")
else:
	print(f'You were {diff} days old on the eve of the new millennium.')