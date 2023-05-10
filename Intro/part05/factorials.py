# Write your solution here
def factorials(n: int):
	k = {}
	k[1] = 1
	i = 1
	prev = 1
	while i <= n:
		k[i] = i * prev
		prev = i * prev
		i += 1

	return k
if __name__ == "__main__":
	k = factorials(5)
	print(k[1])
	print(k[3])
	print(k[5])