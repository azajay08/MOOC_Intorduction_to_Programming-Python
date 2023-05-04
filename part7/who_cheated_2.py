# Write your solution here
from datetime import datetime, timedelta, time

def is_valid(st, sb):
	t1 = datetime.strptime(st[1], "%H:%M")
	t2 = datetime.strptime(sb[3], "%H:%M")
	diff = (t2 - t1).total_seconds() / (60 * 60)
	if diff > 3:
		return False
	return True

def final_points():
	students = {}
	with open("start_times.csv") as s_file:
		start = s_file.read()
	with open("submissions.csv") as subfile:
		submit = subfile.read()
	for line in start.strip().split('\n'):
		grade = 0
		l_split = line.strip().split(';')
		for i in range(9):
			temp_grade = 0
			for sub in submit.strip().split('\n'):
				s_split = sub.strip().split(';')
				if s_split[0] == l_split[0]:
						if i == int(s_split[1]):
							if is_valid(l_split, s_split):
								if int(s_split[2]) > temp_grade:
									temp_grade = int(s_split[2])
			grade += temp_grade
		# print(l_split[0], grade)
		students[l_split[0]] = grade
			
	return students

if __name__ == "__main__":
	final = final_points()
	print(final)