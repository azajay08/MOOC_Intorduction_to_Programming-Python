from functools import reduce

class CourseAttempt:
	def __init__(self, course_name: str, grade: int, credits: int):
		self.course_name = course_name
		self.grade = grade
		self.credits = credits

	def __str__(self):
		return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts):
	return reduce(lambda creds, c: creds + c.credits, attempts, 0)

def sum_of_passed_credits(attempts):
	return reduce(lambda creds, c: creds + c.credits, filter(lambda g : g.grade > 0, attempts), 0)

def average(attempts: list):
	av = list(filter(lambda g : g.grade > 0, attempts))
	reduced = reduce(lambda grades, c: grades + c.grade, av, 0)
	return reduced / len(av)

if __name__ == "__main__":
	s1 = CourseAttempt("Introduction to Programming", 5, 5)
	s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
	s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
	ag = average([s1, s2, s3])
	print(ag)