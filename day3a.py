import math

gridSize = 200
minDist = gridSize * 2
minPath = minDist
middlePoint = math.floor(gridSize / 2)
print(middlePoint)

f = open("./inputs/day3_test1.txt", "r")
fileInput = f.read()

wirepaths = fileInput.split('\n')
path1 = wirepaths[0].split(',')
path2 = wirepaths[1].split(',')
print("1st path is", path1)
print("2nd path is", path2)

grid = [["." for x in range(gridSize)] for y in range(gridSize)]
grid[middlePoint][middlePoint] = "o"

def printGrid(grid):
	grid[middlePoint][middlePoint] = "o"
	i = 0
	while i < gridSize:
		j = 0
		line = ""
		while j < gridSize:
			el = str(grid[i][j])
			line = line + el
			j = j + 1
		print(line)
		i = i + 1
	return

def manhattan(x, y):
	return (abs(x-middlePoint) + abs(y-middlePoint))

def calcStepSize(step):
	if len(step) == 2:
		stepSize = int(step[1])
	elif len(step) == 3:
		stepSize = 10*int(step[1]) + int(step[2])
	elif len(step) == 4:
		stepSize = 100*int(step[1]) + 10*int(step[2]) + int(step[3])
	elif len(step) == 5:
		stepSize = 1000*int(step[1]) + 100*int(step[2]) + 10*int(step[3]) + int(step[4]) 
	return stepSize

reachedEnd = False
i = 0
j = 0
while reachedEnd == False:
	if (i - 1) == len(path1) and (j - 1) == len(path2):
		reachedEnd = True
	else:
		step1 = path1[i]
		step2 = path2[j]
		stepSize1 = calcStepSize(step1)
		stepSize2 = calcStepSize(step2)
		

		for k in range(1, stepSize1 + 1):
		if step1[0] == "R":
			pos_x1 += 1
			grid[pos_y][pos_x] = "-"
		elif step1[0] == "L":
			pos_x -= 1
			grid[pos_y][pos_x] = "-"
		elif step[0] == "U":
			pos_y -= 1
			grid[pos_y][pos_x] = "|"
		elif step[0] == "D":
			pos_y += 1
			grid[pos_y][pos_x] = "|"
		


f.close()