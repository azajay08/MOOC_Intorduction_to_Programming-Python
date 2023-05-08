# Write your solution here
def get_grade(i):
	if i >= 0 and i <= 14:
		return 0
	if i >= 15 and i <= 17:
		return 1
	if i >= 18 and i <= 20:
		return 2
	if i >= 21 and i <= 23:
		return 3
	if i >= 24 and i <= 27:
		return 4
	else:
		return 5

def print_stats(grade, average, percent):
	print("Statistics:")
	print(f"Points average: {average:.1f}")
	print(f"Pass percentage: {percent:.1f}")
	print("Grade distribution:")
	print(" 5:", "*" * grade.count(5))
	print(" 4:", "*" * grade.count(4))
	print(" 3:", "*" * grade.count(3))
	print(" 2:", "*" * grade.count(2))
	print(" 1:", "*" * grade.count(1))
	print(" 0:", "*" * grade.count(0))

def get_stats(exe, exam):
	grade = []
	count = float(len(exe))
	average = 0
	passed = 0
	percent = 0
	x = 0
	for i in exe:
		passed = get_grade(i)
		if exam[x] == 0:
			passed = 0
		x += 1
		grade.append(passed)
		average += i
		if passed > 0:
			percent += 1
	if percent > 0:
		percent = (percent / count) * 100
	average = (average) / count
	print_stats(grade, average, percent)


def main():
	exe = []
	exam = []
	while True:
		scores = (input("Exam points and exercises completed: "))
		if scores:
			score_split = scores.split()
			if int(score_split[0]) < 10:
				exam.append(int(0))
			else:
				exam.append(int(score_split[0]))
			exe.append(int(score_split[0]) + (int(score_split[1]) // 10))
		else:
			get_stats(exe, exam)
			break
	
main()