file = open("input.txt", 'r')
numbers = []
i = 0;
while(True):
	temp = file.readline()
	if(not temp.isspace()):
		if(temp == ""):
			break
		numbers.append(int(temp))
		i += 1
file.close()
print(len(numbers))
print("\n")

#Part 1
done = False
for x in range(len(numbers)):
	if(done):
		break
	for y in range(len(numbers)):

		if(done):
			break

		if(x == y):
			continue

		if(numbers[x] + numbers[y] == 2020):
			print(numbers[x])
			print(numbers[y])
			print("x * y = ")
			print(numbers[x] * numbers[y])
			print("done part 1")
			print("\n")
			done = True

#Part 2
done = False
for x in range(len(numbers)):
	if(done):
		break
	for y in range(len(numbers)):
		if(done):
			break
		for z in range(len(numbers)):
			if(done):
				break

			if(x == y or y == z or x == z):
				continue

			if(numbers[x] + numbers[y] + numbers[z] == 2020):
				print(numbers[x])
				print(numbers[y])
				print(numbers[z])
				print("x * y * z = ")
				print(numbers[x] * numbers[y] * numbers[z])
				print("done part 2")
				print("\n")
				done = True