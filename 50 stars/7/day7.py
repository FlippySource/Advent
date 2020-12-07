file = open("input.txt", 'r')
outerBagToInner = {}
innerBagToOuter = {}

empty = "no other"
while(True):
	line = file.readline().replace("\n", "") 

	if(line == ""):
		break

	rule = line.split(" bags contain ")
	outerBag = rule[0].replace(" bags", "")
	temp = rule[1][:-1].replace(" bags", "")
	temp = temp.replace(" bag", "")
	innerBags = temp.split(", ")

	if(innerBags[0] == empty):
		innerBags = []

	i = 1
	tempBag = outerBag

	while (tempBag in outerBagToInner):
		print("Duplicate rule!")
		i += 1
		tempBag = outerBag + "(variant " + str(i) + ")"

	outerBag = tempBag
	outerBagToInner[outerBag] = innerBags

	for bag in innerBags:
		bagKey = bag[bag.find(" ") + 1:]
		if(not bagKey in innerBagToOuter):
			innerBagToOuter[bagKey] = []
		innerBagToOuter[bagKey].append(outerBag)

file.close()
print(len(outerBagToInner))
print(len(innerBagToOuter))
print("\n")

#Part 1

def getParentBags(inputBag, output):
	if(not inputBag in innerBagToOuter):
		return set()

	outers = innerBagToOuter[inputBag]
	for outer in outers:
		if(outer in output): 
			continue
		output.add(outer)
		getParentBags(outer, output)
			
	return output

goalBag = "shiny gold"
print("Part 1")
print(len(getParentBags(goalBag, set())))
print("\n")

#Part 2
def getDepthCount(inputBag, count, currentMult):
	rule = outerBagToInner[inputBag]
	if(rule == []):
		return count + currentMult
	count += currentMult
	for bagType in rule:
		multiplier = int(bagType[:bagType.find(" ")])
		newType = bagType[bagType.find(" ") + 1:]
		count = getDepthCount(newType, count, currentMult * multiplier)
	return count

startBag = "shiny gold"
finalCount = getDepthCount(startBag, 0, 1) -1

print("Part 2")
print(finalCount)
print("\n")