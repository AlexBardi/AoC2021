file = open("input.txt")

totalCount = 0
for line in file:
    input = line.split()[:10]
    inSets = []
    for entry in input:
        inSet = set()
        for char in entry:
            inSet.add(char)
        inSets.append(inSet)
    numToSet = {}
    toRemove = []
    for inSet in inSets:
        if len(inSet) == 2:
            numToSet[1] = inSet
            toRemove.append(inSet)
        elif len(inSet) == 4:
            numToSet[4] = inSet
            toRemove.append(inSet)
        elif len(inSet) == 3:
            numToSet[7] = inSet
            toRemove.append(inSet)
        elif len(inSet) == 7:
            numToSet[8] = inSet
            toRemove.append(inSet)
    for inSet in toRemove:
        inSets.remove(inSet)

    toRemove = []
    for inSet in inSets:
        if len(inSet) == 6:
            if inSet.issuperset(numToSet[4]):
                numToSet[9] = inSet
                toRemove.append(inSet)
            elif inSet.issuperset(numToSet[1]):
                numToSet[0] = inSet
                toRemove.append(inSet)
            else:
                numToSet[6] = inSet
                toRemove.append(inSet)
    for inSet in toRemove:
        inSets.remove(inSet)

    for inSet in inSets:
        if inSet.issubset(numToSet[9]):
            if numToSet[1].issubset(inSet):
                numToSet[3] = inSet
            else:
                numToSet[5] = inSet
        else:
            numToSet[2] = inSet

    for num in range(10):
        print(num,": ",numToSet[num])
    print()

    output = line.split()[-4:]
    subSum = 0
    for entry in output:
        outSet = set()
        for char in entry:
            outSet.add(char)
        for num in numToSet:
            if numToSet[num] == outSet:
                subSum *= 10
                subSum += num
                break
    totalCount += subSum

print(totalCount)

