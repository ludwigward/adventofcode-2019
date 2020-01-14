import intComputer
from itertools import permutations

perms = permutations([0, 1, 2, 3, 4]) 

ampOut = [0 for i in range(6)]

testPerm = [4,3,2,1,0] #file1
testPerm = [0,1,2,3,4] #file2
testPerm = [1,0,4,3,2] #file3

lastOutput = 0
maxThrust = 0
maxPerm = [0,0,0,0,0]
# Create an array of integers, there's probably a better way...

for perm in perms:
	for amp in range(len(ampOut)-1):

		fileName = "./inputs/day7.txt"
		f = open(fileName, "r")
		fileInput = f.read()
		f.close()

		fileData = []
		testOutputs = []

		fileInput = fileInput.split(',')

		for i in range(len(fileInput)):
			fileData.append(int(fileInput[i]))
		

		print("Trying phases", perm)
		pos = 0
		#Give phase value
		print("----------------")
		print("Round", amp)
		pos, fileData, lastOutput = intComputer.runInstruction(fileData,pos,perm[amp],testOutputs)
		while pos >= 0:
			print("Sending input", ampOut[amp])
			pos, fileData = intComputer.runInstruction(fileData,pos,ampOut[amp],testOutputs)

		ampOut[amp+1] = testOutputs[len(testOutputs)-1]

	print("Thrust is:", max(ampOut))
	if max(ampOut) > maxThrust:
		maxThrust = max(ampOut)
		maxPerm = perm

print("Max thrust is", maxThrust, "at", maxPerm)

print(ampOut)
#print(intComputer.runInstruction(8, ))