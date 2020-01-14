# day2.py
import math

def calculateOutput(unit, fileName):
	f = open(fileName, "r")
	fileInput = f.read()

	fileInput = fileInput.split(',')

	fileData = []
	testOutputs = []
	
	# Create an array of integers, there's probably a better way...

	for i in range(len(fileInput)):
		fileData.append(int(fileInput[i]))

	print(len(fileData), "elements in")
	#print(fileData)

	pos = 0
	while True:
		print("---------------------------------")
		for x in range(len(fileData)):
			print(x,":",fileData[x])
		print("Starting at pos", pos)
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

		print(orgCode, "and gives opcode", opcode, "and modes", modes)

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

			fileData[position] = unit
			print(unit, "stored at position", position)
			pos += 2

		elif opcode == 4:
			if modes[0] == 0:
				position = fileData[pos+1]
			else:
				position = pos + 1
			print("Added output", fileData[position], "from pos=", position)
			testOutputs.append(fileData[position])
			pos += 2

		elif opcode == 5 or opcode == 6:
			if modes[0] == 0:
				params.append(fileData[fileData[pos+1]])
			else:
				params.append(fileData[pos+1])
			if modes[1] == 0:
				params.append(fileData[fileData[pos+2]])
			else:
				params.append(fileData[pos+2])

			print("Params", params)
			if opcode == 5: 
				print("Make comparison", params[0], "!=0")
				if params[0] != 0:
					print("opcode",opcode, "new position", params[1])
					pos = params[1]
				else:
					pos += 3

			elif opcode == 6:
				print("Make comparison", params[0], "==0")
				if params[0] == 0:
					print("opcode",opcode, "new position", params[1])
					pos = params[1]
				else:
					pos += 3

		elif opcode == 7 or opcode == 8:
			if modes[0] == 0:
				params.append(fileData[fileData[pos+1]])
			else:
				params.append(fileData[pos+1])
			if modes[1] == 0:
				params.append(fileData[fileData[pos+2]])
			else:
				params.append(fileData[pos+2])

			if len(modes) == 2:
				modes.append(0)

			if modes[2] == 0:
				params.append(fileData[fileData[pos+3]])
			else:
				params.append(fileData[pos+3])

			outputPos = params[2]
			outputPos = pos+3
			outputPos = fileData[pos+3]

			if opcode == 7:
				print("Make comparison", params[0], "<", params[1])
				if params[0] < params[1]:

					print("Stored 1 in pos", outputPos)
					fileData[outputPos] = 1
				else:
					print("Stored 0 in pos", outputPos)
					#fileData[params[2]] = 0
					#fileData[pos+3] == 1
					fileData[outputPos] = 0

			if opcode == 8:
				print("Make comparison", params[0], "==", params[1])
				if params[0] == params[1]:
					print("Stored 1 in pos", outputPos)
					fileData[outputPos] = 1
				else:
					print("Stored 0 in pos", outputPos)
					#fileData[params[2]] = 0
					fileData[outputPos] = 0

			pos += 4
		print("Modes ", modes)
		#print("Raw   ", )
		print("Params", params)
		print("New pos = ", pos)
		#print(fileData[223])
		print(fileData)

	f.close()
	#print(fileData)
	return testOutputs

#calculateOutput(12,2)
#calculateOutput(12,4)

print(calculateOutput(5, "./inputs/day5.txt"))
		
	
	

