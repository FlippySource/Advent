file = open("input.txt", 'r')
passwordLines = []
i = 0;
while(True):
	temp = file.readline()
	if(not temp.isspace()):
		if(temp == ""):
			break
		passwordLines.append(temp)
		i += 1
file.close()
print(len(passwordLines))
print("\n")

#Part 1
allowed = 0;
disallowed = 0;

for line in passwordLines:
	sides = line.split(':')
	ruleParts = sides[0].split(' ')
	lens = ruleParts[0].split('-')

	countMin = int(lens[0])
	countMax = int(lens[1])
	reqLetter = ruleParts[1]
	password = sides[1].strip(" ")

	count = password.count(reqLetter)

	if(count < countMin or count > countMax):
		disallowed += 1
	else:
		allowed += 1

	#print(password)
	#print(reqLetter)
	#print(countMin)
	#print(countMax)
print("Part 1")
print("Allowed:")
print(allowed)
print("Disallowed:")
print(disallowed)
print("\n")


#Part 2
allowed = 0;
disallowed = 0;

for line in passwordLines:
	sides = line.split(':')
	ruleParts = sides[0].split(' ')
	lens = ruleParts[0].split('-')
	
	pos1 = int(lens[0])
	pos2 = int(lens[1])
	reqLetter = ruleParts[1]
	password = sides[1].strip(" ")

	pos1Match = int(password[pos1 - 1] == reqLetter)
	pos2Match = int(password[pos2 - 1] == reqLetter)

	if(pos1Match + pos2Match == 1):
		allowed += 1
	else:
		disallowed += 1

print("Part 2")
print("Allowed:")
print(allowed)
print("Disallowed:")
print(disallowed)
print("\n")