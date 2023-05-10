# Write your solution here

def add_student(students, name):
	students[name] = {}

def add_course(students, name, course):
	if name in students:
		if 'courses' not in students[name]:
			students[name]['courses'] = []
		subject = [s for s in students[name]['courses'] if s[0] == course[0]]
		if not subject and course[1] != 0:
			students[name]['courses'].append(course)
		elif subject and course[1] > subject[-1][1]:
			students[name]['courses'].remove(subject[-1])
			students[name]['courses'].append(course)
	else:
		print(f"{name}: no such person in the database")

def print_student(students, name):
	if name in students:
		print(f"{name}:")
		if 'courses' in students[name]:
			courses = students[name]['courses']
			if len(courses) != 0:
				print(f" {len(courses)} completed courses:")
			else:
				print(" no completed courses")
			for subject, grade in courses:
				print(f"  {subject} {grade}")
			if (len(courses) != 0):
				average = sum(s[1] for s in courses) / len(courses)
				print(f" average grade {average}")
		else:
			print(" no completed courses")

	else:
		print(f"{name}: no such person in the database")

def summary(students):
	print("students", len(students))
	c_count = 0
	c_name = ""
	best_grade = 0
	best_grade_name = ""
	for name in students:
		courses = students[name]['courses']
		subjects = []
		course_total = 0
		for subject, grade in courses:
			if grade > 0:
				subjects.append(subject)
				course_total += grade
		average = course_total / len(subjects) if subjects else 0
		if len(subjects) > c_count:
			c_count = len(subjects)
			c_name = name
		if average > best_grade:
			best_grade = average
			best_grade_name = name

	print("most courses completed", c_count, c_name)
	print("best average grade", best_grade, best_grade_name)

def kooste(sanakirja):
	print(f"opiskelijoita {len(sanakirja)}")
	eniten_suorituksia = 0
	eniten_suorituksia_nimi = ""
	paras_keskiarvo = 0
	paras_keskiarvo_nimi = ""
    
	for nimi in sanakirja:
		suoritukset = sanakirja[nimi]["suoritukset"]
		kurssit = set()
		suoritukset_summa = 0
		for kurssi, arvosana in suoritukset:
			if arvosana > 0:
				kurssit.add(kurssi)
				suoritukset_summa += arvosana
		keskiarvo = suoritukset_summa / len(kurssit) if kurssit else 0
		
		if len(kurssit) > eniten_suorituksia:
			eniten_suorituksia = len(kurssit)
			eniten_suorituksia_nimi = nimi
		
		if keskiarvo > paras_keskiarvo:
			paras_keskiarvo = keskiarvo
			paras_keskiarvo_nimi = nimi
			
	print("eniten suorituksia", eniten_suorituksia, eniten_suorituksia_nimi)
	print("paras keskiarvo", paras_keskiarvo, paras_keskiarvo_nimi)

if __name__ == "__main__":
	students = {}
	add_student(students, "Peter")
	add_student(students, "Eliza")
	add_course(students, "Peter", ("Data Structures and Algorithms", 1))
	add_course(students, "Peter", ("Introduction to Programming", 1))
	add_course(students, "Peter", ("Advanced Course in Programming", 1))
	add_course(students, "Eliza", ("Introduction to Programming", 5))
	add_course(students, "Eliza", ("Introduction to Computer Science", 4))
	summary(students)