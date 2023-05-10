# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

quad = b ** 2 - 4 * a * c
if quad > 0:
    root1 = (-b + sqrt(quad))/(2 * a)
    root2 = (-b - sqrt(quad))/(2 * a)

print(f"The roots are {root1} and {root2}")