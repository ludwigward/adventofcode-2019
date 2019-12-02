# day2.py

# f = open("./outputDatas/day2.txt", "r")

def calculateOutput(noun, verb):
	f = open("./inputs/day2.txt", "r")
	fileInput = f.read()

	fileInput = fileInput.split(',')

	outputData = []
	
	# Create an array of integers, there's probably a better way...
	i = 0
	while i < len(fileInput):
		outputData.append(int(fileInput[i]))
		i += 1

	outputData[1] = noun
	outputData[2] = verb

	pos = 0
	while True:
		opcode = int(outputData[pos])

		if opcode == 99:
			break
		else:
			input1 = int(outputData[int(outputData[pos+1])])
			#print("input1 is", input1)
			input2 = int(outputData[int(outputData[pos+2])])
			#print("input2 is", input2)
			newPos = int(outputData[pos+3])
			if opcode == 1:
				result = input1 + input2
			elif opcode == 2:
				result = input1*input2
			outputData[newPos] = result

			pos += 4

	f.close()
	return outputData[0]

#calculateOutput(12,2)
#calculateOutput(12,4)

foundMatch = False
target = 19690720
if True:
	noun = -1
	while noun <= 140 and foundMatch == False:
		noun += 1
		verb = 0
		while verb <= 140:
			recentOutput = calculateOutput(noun, verb)
			if recentOutput == target:
				foundMatch = True
				print("Answer = ", noun*100 + verb)
				break
			else:
				verb += 1
		
	
	

