# write your solution here

if True:
	# this is never executed
	student_info = input("Student information: ")
	exercise_data = input("Exercises completed: ")
else:
	# hard-coded input
	student_info = "students1.csv"
	exercise_data = "exercises1.csv"

with open(student_info) as stud:
	pupil = {}
	for line in stud:
		l_split = line.strip().split(";")
		if l_split[0] == 'id':
			continue
		pupil[l_split[0]] = {}
		pupil[l_split[0]]['first'] = l_split[1]
		pupil[l_split[0]]['last'] = l_split[2]
with open(exercise_data) as exe:
	for line in exe:
		l_split = line.strip().split(";")
		if l_split[0] == 'id':
			continue
		exe_count = 0
		if l_split[0] in pupil:
			for num in l_split[1:]:
				exe_count += int(num)
			pupil[l_split[0]]["exec_nbr"] = exe_count

for scores in pupil:
	print(f"{pupil[scores]['first']} {pupil[scores]['last']} {pupil[scores]['exec_nbr']}")

