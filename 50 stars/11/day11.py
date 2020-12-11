file = open("input.txt", 'r')
rows = file.read().split("\n")
file.close()

print(len(rows))
print("\n")

#Part 1
def shouldChange(yCoord, xCoord, currentBoard):
	adjOccupied = 0
	empty = 'L'
	occupied = '#'
	floor = '.'

	current = currentBoard[yCoord][xCoord]
	if current == '.':
		return ''

	for y in range(yCoord - 1, yCoord + 2):
		if(y < 0 or y >= len(currentBoard)):
				continue

		for x in range(xCoord -1, xCoord + 2):
			if(y == yCoord and x == xCoord):
				continue

			if(x < 0 or x >= len(currentBoard[y])):
				continue

			if(currentBoard[y][x] == occupied):
				adjOccupied += 1

	if(adjOccupied == 0 and current == empty):
		return occupied

	if(adjOccupied >= 4 and current == occupied):
		return empty

	return ""


board = rows.copy()
newBoard = board.copy()

hasChange = False
first = True

while hasChange or first:

	hasChange = False
	if first:
		first = False

	for seatY in range(len(board)):
		line = ""
		for seatX in range(len(board[seatY])):
			temp = shouldChange(seatY, seatX, board)
			new = board[seatY][seatX]
			if(temp != ""):
				hasChange = True
				new = temp
			line += new
		newBoard[seatY] = line
	board = newBoard.copy()

occupied = '#'
seated = 0

for i in newBoard:
	seated += i.count(occupied)

print("Part 1")
print(seated)
print("\n")

#Part 2
def shouldChange2(yCoord, xCoord, currentBoard):
	adjOccupied = 0
	empty = 'L'
	occupied = '#'
	floor = '.'

	current = currentBoard[yCoord][xCoord]
	if current == '.':
		return ''

	for yMod in range(-1, 2):
		for xMod in range(-1, 2):
			if(yMod == 0 and xMod == 0):
				continue
			cont = True
			tempY = yCoord
			tempX = xCoord
			while(cont):
				tempX += xMod
				tempY += yMod

				if(tempY < 0 or tempY >= len(currentBoard)):
					break;

				if(tempX < 0 or tempX >= len(currentBoard[tempY])):
					break;

				if(currentBoard[tempY][tempX] != floor):
					if(currentBoard[tempY][tempX] == occupied):
						adjOccupied += 1
					break

	if(adjOccupied == 0 and current == empty):
		return occupied

	if(adjOccupied >= 5 and current == occupied):
		return empty

	return ""


board = rows.copy()
newBoard = board.copy()

hasChange = False
first = True

while hasChange or first:

	hasChange = False
	if first:
		first = False

	for seatY in range(len(board)):
		line = ""
		for seatX in range(len(board[seatY])):
			temp = shouldChange2(seatY, seatX, board)
			new = board[seatY][seatX]
			if(temp != ""):
				hasChange = True
				new = temp
			line += new
		newBoard[seatY] = line
	board = newBoard.copy()

occupied = '#'
seated = 0

for i in newBoard:
	seated += i.count(occupied)

print("Part 2")
print(seated)
print("\n")