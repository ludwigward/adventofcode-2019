# day6.py
fileName = "./inputs/day6.txt"
def objectExists(objList, objName):
	#print("Search for", objName, "in", objList, "Length", len(objList))
	
	ret = False

	if len(objList) == 0:
		#print("Object list empty")
		return False

	#print("List to search in is:", objList)
	for name in objList:
		#print("name=",name,"objName=", objName)
		if objName == name:
			return True

	return False

def getAllObjects():
	f = open(fileName, "r")

	objs = []

	while True:
		rel = f.readline().split(")")
		if len(rel) == 0:
			#print("Reached end")
			break

		#print("Before check", objs)
		
		firObj = rel[0]
		if firObj == "":
			break

		#print("First  obj",firObj)
		secObj = rel[1]
		secObj = secObj[:3]
		#print("Second obj", secObj)
		
		if objectExists(objs, firObj) == False:
			#print("Added", firObj)
			objs.append(firObj)
		if objectExists(objs, secObj) == False:
			#print("Added", secObj)
			objs.append(secObj)
		#print("After check", objs)

	f.close()

	return objs

def findRelations(parent):
	f = open(fileName, "r")
	rel = f.readline().split(")")

	chld = []
	num_lines = sum(1 for line in open(fileName))

	for i in range(num_lines):
		if rel[0] == parent:
			tmp = rel[1]
			tmp = tmp[:3]
			#print("Parent", parent, "has child", tmp)
			chld.append(tmp)
		rel = f.readline().split(")")


	#print(rel)
	i = 0
	#print("chld is", chld)

	return chld

def orbitsToCentre(objName, relations, centreObject):
	path = []
	orbits = 0
	orbitsAround = ""

	if objName == centreObject:
		return path

	while True:
		objPos = 0
		for i in relations:
			for j in i:

				if objName == j:
					orbitsAround = objects[objPos]
					orbits += 1
					path.append(orbitsAround)
					print(j, "orbits around", orbitsAround)
			objPos += 1

		if orbitsAround != centreObject:
			objName = orbitsAround
			orbitsAround = ""
		else:
			break
	print(path, len(path))
	return path

def findCentreObject(objList, relations):
	#cntr = objList[0]
	cntr = ""

	for obj in objList:
		hasRel = False
		for i in relations:
			for j in i:
				if obj == j:
					hasRel = True 
		if hasRel == False:
			return obj


	return cntr

objects = getAllObjects()
#print("ALL OBJECTS", objects)

relations = ["" for x in range(len(objects))]
paths = []

for x in range(len(objects)):
	relations[x] = findRelations(objects[x])
	#print(objects[x], ":", relations[x])

centre = findCentreObject(objects, relations)
print("Center is at", centre)

sanPath = []
youPath = []


total = 0
for x in range(len(objects)):
	#if len(relations[x]) == 0:
	print("Find orbits of", objects[x])
	currPath = orbitsToCentre(objects[x], relations, centre)
	paths.append(currPath)
	print("It has path:", currPath)
	total += len(currPath)
	
	if objects[x] == "SAN":
		sanPath = currPath
	elif objects[x] == "YOU":
		youPath = currPath

	#print(objects[x], relations[x])
	print("Indirect orbits = ", total)

for x in range(len(objects)):
	print(objects[x], ":", relations[x], ":", paths[x])

print(len(youPath))
print(len(sanPath))
print(youPath)

lastObj = ""
for i in range(len(youPath)-1,0,-1):
	for j in range(len(sanPath)):
		print("i=",i,"j=",j)
		if youPath[i] == sanPath[j]:
			print("Similar is:", youPath[i])
			lastObj = youPath[i]
			youPath.pop(i)
			sanPath.pop(j)

#youPath.append(lastObj)
#sanPath.append(lastObj)
print(lastObj)
print(youPath)
print(sanPath)
print("Moves needed is:", (len(youPath) + len(sanPath)))
