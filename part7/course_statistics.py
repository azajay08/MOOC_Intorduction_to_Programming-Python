# Write your solution here
import urllib.request
import json

def retrieve_course(course):
	data = (urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course}/stats"))
	r_file = json.loads(data.read())
	weeks = 0
	stats = {}
	students = 0
	hours = 0
	exs = 0
	for k, v in r_file.items():
		weeks += 1
		hours += int(v['hour_total'])
		exs += int(v['exercise_total'])
		if int(v['students']) > students:
			students = int(v['students'])
	stats['weeks'] = weeks
	stats['students'] = students
	stats['hours'] = hours
	stats['hours_average'] = hours // students
	stats['exercises'] = exs
	stats['exercises_average'] = exs // students
	return stats

def retrieve_all():

	data = (urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses"))
	r_file = json.loads(data.read())
	course_list = []
	for line in r_file:
		if line['enabled'] == True:
			info = (line['fullName'], line['name'], line['year'], sum(line['exercises']))
			course_list.append(info)
	return course_list

if __name__ == "__main__":
	retrieve_all()
	retrieve_course("docker2019")