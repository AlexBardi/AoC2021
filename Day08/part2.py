file = open("input.txt")

diffCount = 0
for line in file:
    input = line.split()[:10]
    inSets = []
    for entry in input:
        inSet = set()
        for char in entry:
            inSet.add(char)
        inSets.append(inSet)
    inDict = {}
    for inSet in inSets:
        if len(inSet) == 2:
            inDict[1] = inSet
        elif len(inSet) == 4:
            inDict[4] = inSet
        elif len(inSet) == 3:
            inDict[7] = inSet
        elif len(inSet) == 7:
            inDict[8] = inSet

    output = line.split()[-4:]
    for digit in output:
        if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
            diffCount += 1

print(diffCount)
