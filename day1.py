import math

print('Starting Day 1')
def calcFuel(mass):
	return math.floor(mass / 3) - 2

# Test the examples
print('12 should give 2, gives', calcFuel(12))
print('14 should give 2, gives', calcFuel(14))
print('1969 should give 654, gives', calcFuel(1969))
print('100756 should give 33583, gives', calcFuel(100756))

f = open("./inputs/day1.txt", "r")

totalFuel = 0

for line in f:
	fuel = calcFuel(int(line))
	additionalFuel = calcFuel(fuel)

	while additionalFuel > 0:
		fuel = fuel + additionalFuel
		additionalFuel = calcFuel(additionalFuel)	 

	totalFuel = totalFuel + fuel

print("Total needed fuel is", totalFuel)

f.close()