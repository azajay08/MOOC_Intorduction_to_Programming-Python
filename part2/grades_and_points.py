# Write your solution here
score = int(input("How many points [0-100]: "))
if score > 100 or score < 0:
	grade = "impossible!"
elif score >= 0 and score <= 49:
	grade = "fail"
elif score <= 59:
	grade = "1"
elif score <= 69:
	grade = "2"
elif score <= 79:
	grade = "3"
elif score <= 89:
	grade = "4"
else:
	grade = "5"
print(f"Grade: {grade}")