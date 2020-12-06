file = open("input.txt", 'r')

groups = file.read().split("\n\n")

print(groups[0].split("\n")[0])

file.close()
print(len(groups))
print("\n")

#Part 1
sum = 0

for group in groups:
	answered = set()
	for person in group.split("\n"):
		for yes in person:
			answered.add(yes)
	sum += len(answered)

print("Part 1")
print("The sum is " + str(sum))
print("\n")

#Part 2
sum = 0

for group in groups:
	answered = {}
	groupSize = 0

	for person in group.split("\n"):
		groupSize += 1

		for yes in person:
			if(not yes in answered):
				answered[yes] = 0
			answered[yes] += 1

	for question in answered.keys():
		if(answered[question] == groupSize):
			sum += 1

print("Part 2")
print("The sum is " + str(sum))
print("\n")