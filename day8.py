width = 25
height = 6
layers = []

grid = [["-" for i in range(width)] for j in range(height)]

for i in range(height): print(grid[i])

fileName = "./inputs/day8.txt"
f = open(fileName, "r")
fileInput = f.read()
f.close()

noOfLayers = int(len(fileInput) / (width*height))

for i in range(noOfLayers):	layers.append(grid)

zerosInLayer = [0 for i in range(noOfLayers)]
onesInLayer = [0 for i in range(noOfLayers)]
twosInLayer = [0 for i in range(noOfLayers)]

for x in range(noOfLayers):
	#print("Layer", x)
	startOfLayer = x*width*height

	for y in range(height):
		for z in range(width):
			pos = startOfLayer + y*width + z
			#print("Position", pos,"(",x,y,z, ") has value", fileInput[pos])
			layers[x][y][z] = fileInput[pos]
			if fileInput[pos] == "0": zerosInLayer[x] += 1
			if fileInput[pos] == "1": onesInLayer[x] += 1
			if fileInput[pos] == "2": twosInLayer[x] += 1

minLayer = zerosInLayer.index(min(zerosInLayer))
print("Layer with least zeros is", zerosInLayer.index(min(zerosInLayer)))

print("Part 1 answer", onesInLayer[minLayer]*twosInLayer[minLayer])

def printImage(pic):
	for y in range(height):
		print()
		for z in range(width):
			if pic[y][z] == "1":
				#print(pic[y][z], end='')
				print("1", end='')
			elif pic[y][z] == "-":
				print("-", end='')
			elif pic[y][z] == "2":
				print("?", end='')
			else:
				print(" ", end='')
	print()


its = 0
picture = [["-" for i in range(width)] for j in range(height)]

printImage(picture)

for z in range(width):
	for y in range(height):
		print(y,z)

		layer = 0
		while picture[y][z] == "-":
			pos = layer*height*width + z*height + y
			print(fileInput[pos])

			if layer == 99:
				picture[y][z] = fileInput[pos]
			if fileInput[pos] == "0" or fileInput[pos] == "1":
				print("Found in layer", layer)
				picture[y][z] = fileInput[pos]
			else:
				layer += 1

print(its)
printImage(picture)
print()