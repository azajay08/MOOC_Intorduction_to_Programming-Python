# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
i_date = input("Starting date: ")
split_date = i_date.strip().split(".")
day = int(split_date[0])
month = int(split_date[1])
year = int(split_date[2])
s_date = datetime(year, month, day)
day_count = int(input("How many days: "))
total_mins = 0
d = {}
print("Please type in screen time in minutes on each day (TV computer mobile):")
for i in range(day_count):
	addition = timedelta(days=i)
	date = (s_date + addition).strftime("%d.%m.%Y")
	s_time = input(f"Screen time {date}: ")
	mins = s_time.strip().split()
	# maybe a try statement?
	total_mins += (int(mins[0]) + int(mins[1]) + int(mins[2]))
	min_spent = [int(mins[0]), int(mins[1]), int(mins[2])]
	d[date] = min_spent
average = total_mins / day_count
with open(filename, "w") as file:
	e_date = (s_date + timedelta(days=day_count - 1)).strftime("%d.%m.%Y")
	date = s_date.strftime("%d.%m.%Y")
	file.write(f"Time period: {date}-{e_date}\n")
	file.write((f"Total minutes: {total_mins}\n"))
	file.write(f"Average minutes: {average:.1f}\n")
	for k, v in d.items():
		file.write(f"{k}: {v[0]}/{v[1]}/{v[2]}\n")
	print("Data stored in file late_june.txt")