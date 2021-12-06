import re
import numpy as np

file = open("input.txt")
p = re.compile(r'\d+')
grid = np.zeros((1000, 1000))
dangerCount = 0

for line in file:
    x1, y1, x2, y2 = p.findall(line)
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if x1 == x2:
        if y1 < y2:
            for y in range(y1, y2+1):
                grid[x1, y] += 1
                if grid[x1, y] == 2:
                    dangerCount += 1
        else:
            for y in range(y2, y1+1):
                grid[x1, y] += 1
                if grid[x1, y] == 2:
                    dangerCount += 1
    elif y1 == y2:
        if x1 < x2:
            for x in range(x1, x2+1):
                grid[x, y1] += 1
                if grid[x, y1] == 2:
                    dangerCount += 1
        else:
            for x in range(x2, x1+1):
                grid[x, y1] += 1
                if grid[x, y1] == 2:
                    dangerCount += 1
    elif (y2-y1) == (x2-x1):
        if x1 < x2:
            for z in range(x2-x1+1):
                grid[x1+z, y1+z] += 1
                if grid[x1+z, y1+z] == 2:
                    dangerCount += 1
        else:
            for z in range(x1-x2+1):
                grid[x2+z,y2+z] += 1
                if grid[x2+z,y2+z] == 2:
                    dangerCount += 1
    elif (y2-y1) == -(x2-x1):
        if x1 < x2: # 1,3 -> 3,1
            for z in range(x2-x1+1):
                grid[x1+z, y1-z] += 1
                if grid[x1+z, y1-z] == 2:
                    dangerCount += 1
        else: # 3,1 -> 1,3
            for z in range(x1-x2+1):
                grid[x1-z, y1+z] += 1
                if grid[x1-z, y1+z] == 2:
                    dangerCount += 1


print(dangerCount)
