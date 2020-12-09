file = open("input.txt", 'r')
numbers = file.read().split("\n")
file.close()

print(len(numbers))
print("\n")

#Part 1
preambleSize = 25

def findSumFromPreamble(goal, preambleIn):
	for first in range(preambleSize):
		for second in range(preambleSize):
			if(first == second):
				continue
			if(int(preamble[first]) + int(preamble[second]) == int(goal)):
				return True
			#print(preamble[first] + preamble[second])
	return False

preamble = numbers[:preambleSize]
preambleIndex = 0
count = 0
invalid = -1
for number in numbers[preambleSize:]:
	if not (findSumFromPreamble(number, preamble)):
		invalid = number
		break
	preamble[preambleIndex] = number
	count +=1
	preambleIndex += 1
	if(preambleIndex >= preambleSize):
		preambleIndex = 0


print("Part 1")
print(invalid)
print("\n")

#Part 2
invalid = int(invalid)
answerStart = -1
answerEnd = -1
for start in range(len(numbers)):
	add = int(numbers[start])
	index = start
	while(add < invalid and index < len(numbers) - 1):
		add += int(numbers[index + 1])
		index += 1

	if(add == invalid and start != index):
		answerStart = start
		answerEnd = index
		break

smallest = numbers[answerStart]
largest = numbers[answerStart]

for i in range(answerStart + 1, answerEnd + 1):
	current = numbers[i]
	if(current < smallest):
		smallest = current
	elif(current > largest):
		largest = current

print("Part 2")
print("Range " + str(answerStart) + " to " + str(answerEnd))
if(answerStart != -1 and answerEnd != -1):
	print("Smallest: " + str(smallest) + " Largest: " + str(largest))
	print("Key: " + str(int(smallest) + int(largest)))
print("\n")