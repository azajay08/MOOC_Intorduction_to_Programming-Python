# Write your solution here
groups = int(input("How many students on the course? "))
size = int(input("Desired group size? "))
form = groups // size
if (groups % size) != 0:
    form += 1
print(f"Number of groups formed: {form}")