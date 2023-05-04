# Write your solution here
import fractions

def fractionate(amount: int):
	frac = []
	for i in range(amount):
		frac.append(fractions.Fraction(1, amount))
	return frac


if __name__ == "__main__":
	for p in fractionate(3):
		print(p)

	print()

	print(fractionate(2))