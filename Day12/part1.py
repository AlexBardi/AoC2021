import re

file = open("input.txt")

caves = []
caverns = {}
for line in file:
    newCs = re.split("-", line[:-1]) # [:-1] removes newline char at the end of each line
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

toVisit = [["start"]]
finishedPathes = 0

while len(toVisit) > 0:
    curPath = toVisit.pop()
    curCave = curPath[-1]
    if curCave == "end":
        finishedPathes += 1
    else:
        for nextCave in caverns[curCave]:
            if (nextCave != "start") and not (re.findall('[a-z]',nextCave) and (nextCave in curPath)):
                toVisit.append(curPath + [nextCave]) 

print(finishedPathes)



    
