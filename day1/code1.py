

# init variables
listA = []
listB = []
diffList = []
output = 0

# open file, and separate the numbers out into their own lists
with open('day1/input.txt') as inputFile:
    for line in inputFile:
        listA.append(int(line.split()[0]))
        listB.append(int(line.split()[1]))


# sort these lists
listA.sort()
listB.sort()

# find the differences and add them together
for index in range(len(listA)):
    output += abs(listA[index] - listB[index])


print(output)