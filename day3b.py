import math

gridSize = 500
minDist = gridSize * 2
middlePoint = math.floor(gridSize / 2)

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

def plotTrace(grid, step, pos_x, pos_y):
	if len(step) == 2:
		stepSize = int(step[1])
	elif len(step) == 3:
		stepSize = 10*int(step[1]) + int(step[2])
	elif len(step) == 4:
		stepSize = 100*int(step[1]) + 10*int(step[2]) + int(step[3])
	elif len(step) == 5:
		stepSize = 1000*int(step[1]) + 100*int(step[2]) + 10*int(step[3]) + int(step[4]) 


	grid[pos_y][pos_x] = "x"

	for i in range(1, stepSize + 1):
		if step[0] == "R":
			pos_x += 1
			grid[pos_y][pos_x] = "-"
		elif step[0] == "L":
			pos_x -= 1
			grid[pos_y][pos_x] = "-"
		elif step[0] == "U":
			pos_y -= 1
			grid[pos_y][pos_x] = "|"
		elif step[0] == "D":
			pos_y += 1
			grid[pos_y][pos_x] = "|"

	return grid, pos_x, pos_y


# The actual program
f = open("./inputs/day3_test1.txt", "r")
fileInput = f.read()

grid1 = [["." for x in range(gridSize)] for y in range(gridSize)] 
grid2 = [["." for x in range(gridSize)] for y in range(gridSize)] 

# Set the central port to middle

grid1[middlePoint][middlePoint] = "o"
grid2[middlePoint][middlePoint] = "o"


wirepaths = fileInput.split('\n')
path1 = wirepaths[0].split(',')
path2 = wirepaths[1].split(',')
print("1st path is", path1)
print("2nd path is", path2)

pos_x = middlePoint
pos_y = middlePoint
for step in path1:
	grid1, pos_x, pos_y = plotTrace(grid1, step, pos_x, pos_y)

#printGrid(grid)

pos_x = middlePoint
pos_y = middlePoint

commonGrid = grid1

stepCounter = 0
for step in path2:
	grid2, pos_x, pos_y = plotTrace(grid2, step, pos_x, pos_y)


for y in range(gridSize):
	for x in range(gridSize):
		if grid1[y][x] == "-" or grid2[y][x] == "-":
			commonGrid[y][x] = "-"
		elif grid1[y][x] == "|" or grid2[y][x] == "|":
			commonGrid[y][x] = "|"
		elif grid1[y][x] == "x" or grid2[y][x] == "x":
			commonGrid[y][x] = "x"

		if (grid1[y][x] == "-" and grid2[y][x] == "|") or (grid1[y][x] == "|" and grid2[y][x] == "-"):
			if manhattan(x,y) > 0:
				print("Found intersection at x:", x, "y:", y, "Manhattan:", manhattan(x,y))
				minDist = min(manhattan(x, y), minDist)

				commonGrid[y][x] = "X"

commonGrid[middlePoint][middlePoint] = "o"


#printGrid(grid1)
#printGrid(commonGrid)
print("Min distance is:", minDist)

f.close()