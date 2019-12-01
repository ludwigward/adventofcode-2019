import math

print('Starting Day 1')
def calcFuel(mass):
	fuel = mass / 3
	fuel = math.floor(fuel)
	fuel = fuel - 2

	#print(fuel)
	return fuel

# Test the examples
print('12 should give 2, gives', calcFuel(12))
print('14 should give 2, gives', calcFuel(14))
print('1969 should give 654, gives', calcFuel(1969))
print('100756 should give 33583, gives', calcFuel(100756))

inputs = [110756
,132543
,57911
,58262
,119938
,58581
,52446
,127591
,132449
,82732
,51388
,115723
,67376
,61402
,71379
,99264
,54697
,120877
,130457
,89519
,92846
,121983
,145752
,57606
,136613
,74147
,142443
,91993
,66409
,71590
,74057
,126005
,103231
,104401
,105004
,100771
,60204
,125178
,132927
,97615
,116662
,91806
,74435
,69993
,77268
,124654
,116862
,79505
,132479
,104118
,59975
,133267
,71379
,136031
,64325
,85017
,149922
,148287
,62061
,92790
,81205
,74146
,116381
,78975
,66557
,74568
,77797
,60262
,111913
,53703
,139663
,65642
,90693
,105015
,147887
,139533
,97861
,68607
,146757
,97707
,148185
,87966
,115839
,118377
,71123
,82938
,63957
,76062
,144141
,138096
,132460
,67338
,142338
,76347
,128877
,104797
,104637
,107605
,66506
,127296]

testInputs = [12,14,1969,100756]

print('Calculate total fuel needed')
totalFuel = 0
#for i in testInputs:
for i in inputs:
	fuel = calcFuel(i)
	additionalFuel = calcFuel(fuel)
	while additionalFuel > 0:
		fuel = fuel + additionalFuel
		additionalFuel = calcFuel(additionalFuel)
	print(fuel)
	totalFuel = totalFuel + fuel
print(totalFuel)