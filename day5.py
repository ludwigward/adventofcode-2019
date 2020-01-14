# day2.py
import math

# f = open("./fileDatas/day2.txt", "r")

def calculateOutput(unit):
	f = open("./inputs/day5.txt", "r")
	fileInput = f.read()

	fileInput = fileInput.split(',')

	fileData = []
	testOutputs = []
	
	# Create an array of integers, there's probably a better way...

	for i in range(len(fileInput)):
		fileData.append(int(fileInput[i]))

	print(len(fileData), "elements in", fileData)

	pos = 0
	while True:
		code = int(fileData[pos])
		orgCode = code
		opcode = int(code%100)
		modes = [0,0]
		params = []
		
		code -= opcode
		code =int(code/100)

		i = 0
		while code != 0:
			modes[i] = code%10
			code = int(code/10)
			i += 1

		print("Starting at pos", pos, "with", orgCode, "and opcode", opcode)

		if opcode == 99:
			print("Reached end, last output")
			break

		
		
		if opcode == 1 or opcode == 2:
			if modes[0] == 0:
				params.append(fileData[fileData[pos+1]])
			else:
				params.append(fileData[pos+1])
			if modes[1] == 0:
				params.append(fileData[fileData[pos+2]])
			else:
				params.append(fileData[pos+2])
			
			if opcode == 1:
				result = params[0] + params[1]
				print(params[0], "+", params[1], "=", result, "stored at", fileData[pos+3])
			else:
				result = params[0] * params[1]
				print(params[0], "*", params[1], "=", result, "stored at", fileData[pos+3])

			fileData[fileData[pos+3]] = result
			
			pos += 4

		elif opcode == 3:
			position = fileData[pos + 1]

			print("Old value", fileData[position])
			fileData[position] = unit
			print(unit, "stored at position", position)
			print("New value", fileData[position])
			pos += 2

		elif opcode == 4:
			position = fileData[pos+1]
			print("Added output", fileData[position])
			testOutputs.append(fileData[position])
			pos += 2
	
	while False:
		opcode = int(fileData[pos])

		if opcode == 99:
			break
		else:
			input1 = int(fileData[int(fileData[pos+1])])
			#print("input1 is", input1)
			input2 = int(fileData[int(fileData[pos+2])])
			#print("input2 is", input2)
			newPos = int(fileData[pos+3])
			if opcode == 1:
				result = input1 + input2
			elif opcode == 2:
				result = input1*input2
			elif opcode == 3:
				print("3")
			elif opcode == 4:
				print("4")
			fileData[newPos] = result

			pos += 4

	f.close()
	return testOutputs

#calculateOutput(12,2)
#calculateOutput(12,4)

print(calculateOutput(1))
		
	
	

