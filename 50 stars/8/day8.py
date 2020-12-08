file = open("input.txt", 'r')
instructions = file.read().split("\n")
file.close()

print(len(instructions))
print("\n")

#Part 1
nop = "nop"
acc = "acc"
jmp = "jmp"

instructionsRun = set()
noRepeats = True
index = 0
number = 0

while(noRepeats):
	instructionsRun.add(index)

	line = instructions[index]
	split = line.split(" ")
	instruction = split[0]
	if(instruction == nop):
		index +=1

	else:
		value = int(split[1].replace("+", ""))
		if(instruction == acc):
			number += value
			index += 1
		elif(instruction == jmp):
			index += value
			if(index < 0 or index >= len(instructions)):
				print("Index jumped out of bounds!")
				break;
		else:
			print("Invalid instruction: " + instruction)
	if(index in instructionsRun):
		noRepeats = False

print("Part 1")
print("Accumulator: " + str(number))
print("\n")

#Part 2
nop = "nop"
acc = "acc"
jmp = "jmp"

swapper = {
	jmp:nop,
	nop:jmp
}

answer = -1
for i in range(len(instructions)):
	if not instructions[i].startswith(acc):
		instructionsRun = set()
		noRepeats = True
		outOfBounds = False;
		index = 0
		number = 0

		while(noRepeats and index < len(instructions)):
			instructionsRun.add(index)

			line = instructions[index]
			split = line.split(" ")
			instruction = split[0]

			if(index == i):
				instruction = swapper[instruction]

			if(instruction == nop):
				index +=1

			else:
				value = int(split[1].replace("+", ""))
				if(instruction == acc):
					number += value
					index += 1
				elif(instruction == jmp):
					index += value
					if(index < 0 or index > len(instructions)):
						outOfBounds = True
						break;
				else:
					print("Invalid instruction: " + instruction)
			if(index in instructionsRun):
				noRepeats = False
		if(noRepeats == True and outOfBounds == False):
			answer = i
			break;

print("Part 2")
print("Corrupted index: " + str(answer))
print("Accumulator: " + str(number))
print("\n")