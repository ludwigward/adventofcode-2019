import intComputer
from itertools import permutations

perms = permutations([5, 6, 7, 8, 9]) 

ampOut = [0 for i in range(6)]

testPerm = [4,3,2,1,0] #file1
testPerm = [0,1,2,3,4] #file2
testPerm = [1,0,4,3,2] #file3

maxThrust = 0
maxPerm = [0,0,0,0,0]

fileName = "./inputs/day7_test4.txt"
f = open(fileName, "r")
fileInput = f.read()
fileInput = fileInput.split(',')
f.close()

testOutputs = [] 

fileData = [[0 for x in range(len(fileInput))] for y in range(len(ampOut)-1)] 
# Gives format [amp][parameter]


for amp in range(len(ampOut)-1):
	for i in range(len(fileInput)):
		fileData[amp][i] = int(fileInput[i])
print(fileData)

perm = [9,8,7,6,5]
#for perm in perms:
for amp in range(len(ampOut)-1):
	print("Trying phases", perm)

	pos = 0
	#Give phase value
	print("----------------")
	print("On aplifier", amp)
	pos, fileData[amp], lastOutput = intComputer.runInstruction(fileData[amp],pos,perm[amp],0)
	while pos >= 0:
		print("Sending input", ampOut[amp])
		pos, fileData[amp], lastOutput = intComputer.runInstruction(fileData[amp],pos,ampOut[amp],0)

	#ampOut[amp+1] = testOutputs[len(testOutputs)-1]

print("Thrust is:", max(ampOut))
if max(ampOut) > maxThrust:
	maxThrust = max(ampOut)
	maxPerm = perm

print("Max thrust is", maxThrust, "at", maxPerm)


#print(intComputer.runInstruction(8, ))