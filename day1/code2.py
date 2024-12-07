

# init variables
listA = []
listB = []
simularityScores = []
output = 0

# open file, and separate the numbers out into their own lists
with open('day1/input.txt') as inputFile:
    for line in inputFile:
        listA.append(int(line.split()[0]))
        listB.append(int(line.split()[1]))


# sort these lists for fun
listA.sort()
listB.sort()

# for each item in listA find how many times its in list B
for index in range(len(listA)):
    
    currentNumber = listA[index]
    count = 0
    for item in listB:
        if item == currentNumber:
            count += 1
    
    simularityScores.append(currentNumber * count)

for score in simularityScores:
    output += score


print(output)