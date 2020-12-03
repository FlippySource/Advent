file = open("input.txt", 'r')
horizontalSlices = []
i = 0;
while(True):
	temp = file.readline()
	if(not temp.isspace()):
		if(temp == ""):
			break
		horizontalSlices.append(temp.strip())
		i += 1
file.close()
print(len(horizontalSlices))
print("\n")

#Part 1
tree = '#'
snow = '.'

treeCount = 0

verticalSpeed = 1
horizontalSpeed = 3

#dont check 0,0
positionX = horizontalSpeed
positionY = verticalSpeed

while(positionY < len(horizontalSlices)):
	if (positionX >= len(horizontalSlices[positionY])):
		positionX -= len(horizontalSlices[positionY])

	tempChar = horizontalSlices[positionY][positionX]
	if(tempChar == tree):
		treeCount += 1
	elif(tempChar != snow):
		print("invalid char! " + tempChar)

	positionY += verticalSpeed
	positionX += horizontalSpeed

print("Part 1")
print(str(treeCount) + " Trees Hit")


#Part 2
def howManyTreesDoIHit(speedX, speedY):
	tree = '#'
	snow = '.'

	treeCount = 0

	verticalSpeed = speedY
	horizontalSpeed = speedX

	#dont check 0,0
	positionX = horizontalSpeed
	positionY = verticalSpeed

	while(positionY < len(horizontalSlices)):
		if (positionX >= len(horizontalSlices[positionY])):
			positionX -= len(horizontalSlices[positionY])

		tempChar = horizontalSlices[positionY][positionX]
		if(tempChar == tree):
			treeCount += 1
		elif(tempChar != snow):
			print("invalid char! " + tempChar)

		positionY += verticalSpeed
		positionX += horizontalSpeed

	print("with slope (" + str(speedX) + "," + str(speedY) + ")")
	print(str(treeCount) + " Trees Hit")
	print("\n")
	return treeCount


print("Part 2")
mult = 1
mult *= howManyTreesDoIHit(1, 1)
mult *= howManyTreesDoIHit(3, 1)
mult *= howManyTreesDoIHit(5, 1)
mult *= howManyTreesDoIHit(7, 1)
mult *= howManyTreesDoIHit(1, 2)
print("Multiplied answer: " + str(mult))