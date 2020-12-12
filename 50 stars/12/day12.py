file = open("input.txt", 'r')
directions = file.read().split("\n")
file.close()

print(len(directions))
print("\n")

#Part 1
N = 0
S = 180
E = 90
W = 270

heading = E

def turn(direction, amount, heading):
	left = 'L'
	if(direction == left):
		amount *= -1

	heading += amount

	while(heading >= 360):
		heading -= 360

	while(heading < 0):
		heading += 360

	return heading

#Only in units of 90 degrees
turns = [
'L',
'R'
]

compass = {
	'N':N,
	'S':S,
	'E':E,
	'W':W
}

forward = 'F'

shipX = 0
shipY = 0

def changePos(direction, amount, posX, posY):
	if(direction == N):
		posY += amount
		return (posX, posY)

	if(direction == S):
		posY -= amount
		return (posX, posY)

	if(direction == E):
		posX += amount
		return (posX, posY)
		
	if(direction == W):
		posX -= amount
		return (posX, posY)

for direction in directions:
	identifier = direction[0]
	change = int(direction[1:])

	if(identifier in compass):
		out = changePos(compass[identifier], change, shipX, shipY)
		shipX = out[0]
		shipY = out[1]

	elif(identifier in turns):
		if(change % 90 != 0):
			print("non-compass turn: " + str(change))
		heading = turn(identifier, change, heading)

	elif(identifier == forward):
		out = changePos(heading, change, shipX, shipY)
		shipX = out[0]
		shipY = out[1]

print("Part 1")
print("Manhattan distance: " + str(abs(shipX) + abs(shipY)))
print("\n")

#Part 2
N = 0
S = 180
E = 90
W = 270

def turnWaypoint(direction, amount, relativeX, relativeY):
	turn = 1
	left = 'L'
	newX = relativeX
	newY = relativeY

	if(direction == left):
		turn *= -1

	start = -1
	if(newX >= 0 and newY >= 0):
		start = 0
	elif(newX >= 0 and newY <= 0):
		start = 1
	elif(newX <= 0 and newY <= 0):
		start = 2
	elif(newX <= 0 and newY >= 0):
		start = 3
	else:
		return (newX, newY)

	turnMults = [
	(1,1),
	(1,-1),
	(-1, -1),
	(-1, 1)
	]

	rotates = (amount / 90) * turn
	start += rotates

	size = len(turnMults)
	while(start < 0):
		start += size
	while(start >= size):
		start -= size

	if(amount == 90 or amount == 270):
		newX = relativeY
		newY = relativeX

	newX = abs(newX) * turnMults[int(start)][0]
	newY = abs(newY) * turnMults[int(start)][1]

	return (newX, newY)

#Only in units of 90 degrees
turns = [
'L',
'R'
]

compass = {
	'N':N,
	'S':S,
	'E':E,
	'W':W
}

forward = 'F'

shipX = 0
shipY = 0
waypointRelX = 10
waypointRelY = 1

def changeWaypointPos(direction, amount, posX, posY):
	if(direction == N):
		posY += amount
		return (posX, posY)

	if(direction == S):
		posY -= amount
		return (posX, posY)

	if(direction == E):
		posX += amount
		return (posX, posY)
		
	if(direction == W):
		posX -= amount
		return (posX, posY)



for direction in directions:
	identifier = direction[0]
	change = int(direction[1:])

	if(identifier in compass):
		out = changeWaypointPos(compass[identifier], change, waypointRelX, waypointRelY)
		waypointRelX = out[0]
		waypointRelY = out[1]

	elif(identifier in turns):
		if(change % 90 != 0):
			print("non-compass turn: " + str(change))
		out = turnWaypoint(identifier, change, waypointRelX, waypointRelY)
		waypointRelX = out[0]
		waypointRelY = out[1]

	elif(identifier == forward):
			shipX += waypointRelX * change
			shipY += waypointRelY * change

print("Part 2")
print("Manhattan distance: " + str(abs(shipX) + abs(shipY)))
print("\n")
