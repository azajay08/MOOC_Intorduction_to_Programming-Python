# tee ratkaisu tänne
# wwite your solution here

# write your solution here

def get_grade(points):
	if points >= 0 and points <= 14:
		return 0
	elif points <= 17:
		return 1
	elif points <= 20:
		return 2
	elif points <= 23:
		return 3
	elif points <= 27:
		return 4
	else:
		return 5
	
if True:
	# this is never executed
	student_info = input("Student information: ")
	exercise_data = input("Exercises completed: ")
	exam_points= input("Exam points: ")
	course = input("Course information: ")
else:
	# hard-coded input
	student_info = "students1.csv"
	exercise_data = "exercises1.csv"
	exam_points = "exam_points1.csv"
	course = "course1.txt"

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
			pupil[l_split[0]]["exec_pts."] = int((exe_count / 40) * 100 // 10)
with open(exam_points) as exa:
	for line in exa:
		l_split = line.strip().split(";")
		if l_split[0] == 'id':
			continue
		exa_count = 0
		if l_split[0] in pupil:
			exe_points = pupil[l_split[0]]['exec_pts.']
			# print(int(exe_points))
			for num in l_split[1:]:
				exa_count += int(num)
			pupil[l_split[0]]["exm_pts."] = exa_count
			pupil[l_split[0]]["grade"] = get_grade(exa_count + int(exe_points))
			pupil[l_split[0]]["total_pts."] = int(exa_count + exe_points)

with open(course) as crs:
	for line in crs:
		if "name" in line:
			name = line.split(":")[1].strip()
		else:
			pts = int(line.strip().split(":")[1])
	course_str = (f"{name}, {pts} credits")
with open("results.txt", "w") as res_txt:
	res_txt.write(course_str + '\n')
	res_txt.write("=" * len(course_str) + '\n')
	res_txt.write(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}\
{'tot_pts.':<10}grade\n")
	for scores in pupil:
		name = pupil[scores]['first'] + " " + pupil[scores]['last']
		res_txt.write(f"{name:<30}{pupil[scores]['exec_nbr']:<10}{pupil[scores]['exec_pts.']:<10}\
{pupil[scores]['exm_pts.']:<10}{pupil[scores]['total_pts.']:<10}{pupil[scores]['grade']}\n")
print("Results written to files results.txt and results.csv")
with open("results.csv", "w") as results:
	for pup in pupil:
		results.write(f"{pup};{pupil[pup]['first']} {pupil[pup]['last']};{pupil[pup]['grade']}\n")

