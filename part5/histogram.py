# Write your solution here
def histogram(str1):
	d = {}
	for i in str1:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	for key, value in d.items():
		print(key, '*' * value)

if __name__ == "__main__":
	histogram("statistically")
	histogram("abba")