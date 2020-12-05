import math

file = open("input.txt", 'r')
seats = []
seats = file.read().split("\n")
file.close()
print(len(seats))
print("\n")

#Part 1
def getRow(seatId):
	currentFront = 0
	currentBack = 127
	for i in range(7):
		halfChar = seatId[i]
		if(halfChar == 'F'):
			currentBack -= math.ceil((currentBack - currentFront +1) / 2)
		elif(halfChar == 'B'):
			currentFront += math.ceil((currentBack - currentFront +1) / 2)
	return currentFront

def getCol(fullSeatId):
	offset = 7
	currentLeft = 0
	currentRight = 7
	for i in range(3):
		halfChar = fullSeatId[i + offset]
		if(halfChar == 'L'):
			currentRight -= math.ceil((currentRight - currentLeft +1) / 2)
		elif(halfChar == 'R'):
			currentLeft += math.ceil((currentRight - currentLeft +1) / 2)
	return currentLeft

highestId = -1;
for seat in seats:
	row = getRow(seat)
	col = getCol(seat)
	seatId = row * 8 + col

	if(highestId < seatId):
		highestId = seatId

print("Part 1")
print(str(highestId))
print("\n")

#Part 2
rowsToCols = {}

for seat in seats:
	row = getRow(seat)
	col = getCol(seat)
	if not row in rowsToCols:
		rowsToCols[row] = []
	rowsToCols[row].append(col)

myRow = -1
myCol = -1
maxCol = 7
done = False

for row in rowsToCols.keys():
	if(done):
		break
	if(len(rowsToCols[row]) == 7):
		cols = rowsToCols[row]
		cols.sort()
		for i in range(1,8):
			if(not i in cols):
				myRow = row
				myCol = i
				done = True
				break;

print("Part 2")
print("My Row is: " + str(myRow))
print("My Col is: " + str(myCol))
print("My ID is: " + str(myRow * 8 +  myCol))
print("\n")