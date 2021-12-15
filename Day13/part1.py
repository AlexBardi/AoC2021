import re

from numpy.lib.function_base import append

file = open("input.txt")

points = []
dots = True

for line in file:
    if line == '\n':
        dots = False
    elif dots:
        point = re.findall("\d+", line)
        x = int(point[0])
        y = int(point[1])
        points.append((x,y))
    else:
        dir = line[11]
        divNum = int(line[13:])
        break

newlist = []
if dir == 'x':
    for x,y in points:
        if x > divNum:
            diff = x - divNum
            newX = divNum - diff
            if not (newX,y) in newlist:
                newlist.append((newX,y))
        else:
            if not (x,y) in newlist:
                newlist.append((x,y))
else:
    for x,y in points:
        if y > divNum:
            diff = y - divNum
            newY = divNum - diff
            if not (x,newY) in newlist:
                newlist.append((x,newY))
        else:
            if not (x,y) in newlist:
                newlist.append((x,y))
print(len(newlist))