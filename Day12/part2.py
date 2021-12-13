import re

file = open("input.txt")

caves = []
caverns = {}
for line in file:
    # [:-1] removes newline char at the end of each line
    newCs = re.split("-", line[:-1])
    caves.append(newCs[0])
    caves.append(newCs[1])
    if newCs[0] in caverns:
        caverns[newCs[0]].append(newCs[1])
    else:
        caverns[newCs[0]] = [newCs[1]]
    if newCs[1] in caverns:
        caverns[newCs[1]].append(newCs[0])
    else:
        caverns[newCs[1]] = [newCs[0]]

toVisit = [(["start"],False)]
finishedPathes = 0

while len(toVisit) > 0:
    curPath,doub = toVisit.pop()
    curCave = curPath[-1]
    if curCave == "end":
        finishedPathes += 1
    else:
        for nextCave in caverns[curCave]:
            if (nextCave != "start"):
                if re.findall('[A-Z]', nextCave):
                    toVisit.append((curPath + [nextCave],doub))
                elif nextCave != 'start':
                    if doub and not (nextCave in curPath):
                        toVisit.append((curPath + [nextCave],True))
                    elif not doub and not (nextCave in curPath):
                        toVisit.append((curPath + [nextCave],False))
                    elif not doub and (nextCave in curPath):
                        toVisit.append((curPath + [nextCave],True))



print(finishedPathes)
