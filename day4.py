# day4.py
import math

lowerLimit = 666699
upperLimit = 666905

#lowerLimit = 307237
#upperLimit = 769058

lowerLimit = 123400
upperLimit = 123445

def possiblePassword(password):
	onlyIncrease = True
	hasDouble = False
	noLargerDouble = True
	doubleMatches = [0, 0, 0, 0, 0] 

	split = [(password//(10**i))%10 for i in range(math.ceil(math.log(password, 10))-1, -1, -1)]
	#print(split)

	for i in range(1,len(split)):
		if split[i-1] > split[i]:
			onlyIncrease = False
		#print(split[i-1], split[i], onlyIncrease)

		if split[i-1] == split[i]:
			doubleMatches[i-1] = split[i]
			hasDouble = True

	if onlyIncrease and hasDouble:
		for x in range(0, len(doubleMatches) - 1):
			if doubleMatches[x] != 0:

				if doubleMatches[x] == doubleMatches[x+1]:
					print("Match at x=",x, "and x+1:", doubleMatches[x])
					noLargerDouble = False
					if doubleMatches[x] < max(doubleMatches):
						noLargerDouble = True
						print(password, doubleMatches, doubleMatches[x], x, max(doubleMatches))	
						print(doubleMatches[x], max(doubleMatches))

	print(password, onlyIncrease, hasDouble, noLargerDouble)
	return (onlyIncrease and hasDouble and noLargerDouble)


# The code
223450
print("Test 112233: True", possiblePassword(112233))
print("Test 123444: False", possiblePassword(123444))
print("Test 111122: True", possiblePassword(111122))
print("-------------------------------------------")

possibleMatches = 0
for pswd in range(lowerLimit, upperLimit + 1):	

	if possiblePassword(pswd):
		possibleMatches += 1
		print(possibleMatches)

print("Possible matches:", possibleMatches)