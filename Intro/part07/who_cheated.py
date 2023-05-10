# Write your solution here
from datetime import datetime, timedelta, time

def cheaters():
	with open("start_times.csv") as s_file:
		start = s_file.read()
		with open("submissions.csv") as subfile:
			submit = subfile.read()
			students = []
			for line in start.strip().split('\n'):
				l_split = line.strip().split(';')
				t1 = datetime.strptime(l_split[1], "%H:%M")
				for sub in submit.strip().split('\n'):
					s_split = sub.strip().split(';')
					if s_split[0] == l_split[0]:
						# print(s_split)
						t2 = datetime.strptime(s_split[3], "%H:%M")
						diff = (t2 - t1).total_seconds() / (60 * 60)
						# print(l_split[0])
						print(diff)
						if diff > 3:
							if l_split[0] not in students:
								students.append(l_split[0])
						# print(diff)
				# print(line)

	return students

if __name__ == "__main__":
	cheats = cheaters()
	print(cheats)