file = open("input.txt", 'r')
joltages = file.read().split("\n")
file.close()

for i in range(len(joltages)):
	joltages[i] = int(joltages[i])

print(len(joltages))
print("\n")

#Part 1
joltages.sort()
ones = 1
threes = 1
for i in range(len(joltages) -1):
	this = joltages[i]
	next = joltages[i+1]
	if(this + 1 == next):
		ones += 1
	if(this + 3 == next):
		threes += 1

print("Part 1")
print(ones * threes)
print("\n")

#Part 2
counts = []
endpoint = joltages[len(joltages) -1]
for i in reversed(range(len(joltages))):
	this = joltages[i]

	duplicates = i
	while(duplicates >= 0 and joltages[duplicates] == this):
		duplicates -= 1
	duplicates = (i - duplicates) -1 

	maximum = this + 3
	j = i + 1
	count = 0

	while(j < len(joltages) - 1 and joltages[j] <= maximum):
		count += counts[(len(joltages) - 1) - j]
		j += 1

	if(this + 3 >= endpoint):
		count += 1

	if(duplicates >= 1):
		count *= duplicates

	counts.append(count)

counts.reverse()

fullCount = 0
i = 0
maximum = 3
while(joltages[i] <= maximum):
	print(joltages[i])
	fullCount += counts[i]
	i += 1

print("Part 2")
print(fullCount)
print("\n")