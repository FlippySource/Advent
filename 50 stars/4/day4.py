file = open("input.txt", 'r')
passports = []
i = 0;
temp = file.read()
passports = temp.split("\n\n")
print(passports[0].replace("\n", " "))
file.close()
print(len(passports))
print("\n")

#Part 1
requiredParts = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]#, "cid"]

valid = 0
invalid = 0

for passport in passports:
	failed = False;
	pairs = passport.replace("\n", " ").split(" ")
	fields = []
	for pair in pairs:
		fields.append(pair.split(":")[0])
	for field in requiredParts:
		if(not field in fields):
			invalid += 1
			failed = True;
			break
	if(not failed):
		valid += 1

print("Part 1")
print("Valid: " + str(valid))
print("Invalid: " + str(invalid))
print("\n")

#Part 2
requiredParts = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]#, "cid"]
eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

valid = 0
invalid = 0

for passport in passports:
	pairs = passport.replace("\n", " ").split(" ")
	fields = {}
	for pair in pairs:
		temp = pair.split(":")
		if(temp[0] in requiredParts):
			fields[temp[0]] = temp[1]

	if(len(fields) < len(requiredParts)):
		invalid += 1
		continue

	keys = fields.keys()

	for field in requiredParts:
		if field not in keys:
			invalid +=1
			failed = True
			break

	failed = False
	for field in fields.keys():
		value = fields[field]

		if(field == "byr"):
			if(not value.isdigit() or int(value) < 1920 or int(value) > 2002 ):
				invalid +=1
				failed = True
				break

			else:
				continue

		if(field == "iyr"):
			if(not value.isdigit() or int(value) < 2010 or int(value) > 2020 ):
				invalid +=1
				failed = True
				break
				
			else:
				continue

		if(field == "eyr"):
			if(not value.isdigit() or int(value) < 2020 or int(value) > 2030 ):
				invalid +=1
				failed = True
				break
				
			else:
				continue

		if(field == "hgt"):

			label = value[-2:]
			number = value[:-2]

			if(not number.isdigit()):
				invalid +=1
				failed = True
				break
			number = int(number)

			if(label == "cm" and number >= 150 and number <= 193):
				continue

			if(label == "in"and number >= 59 and number <= 76):
				continue
				
			failed = True
			invalid +=1
			break

		if(field == "hcl"):
			if(value[0] != '#' or not value[1:].isalnum()):
				invalid +=1
				failed = True
				break
				
			else:
				continue

		if(field == "ecl"):
			if(not value in eyeColors):
				invalid +=1
				failed = True
				break
				
			else:
				continue

		if(field == "pid"):
			#print(value)
			if(len(value) != 9 or not value.isdigit()):
				invalid +=1
				failed = True
				break
				
			else:
				continue
	if(not failed):
		valid += 1	

print("Part 2")
print("Valid: " + str(valid))
print("Invalid: " + str(invalid))
print("\n")