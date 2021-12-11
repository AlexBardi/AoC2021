import numpy as np

def flash(grid):
    flashCount = 0
    bloomed = []
    while True:
        for x in range(1,11):
            for y in range(1,11):
                if grid[x][y] > 9 and ((x,y) not in bloomed):
                    bloom(grid,x,y)
                    bloomed.append((x,y))
        if flashCount != len(bloomed):
            flashCount = len(bloomed)
        else:
            break
    for point in bloomed:
        x = point[0]
        y = point[1]
        grid[x][y] = 0
    return flashCount


def bloom(grid,x,y):
    grid[x-1][y-1] += 1
    grid[x-1][y] += 1
    grid[x-1][y+1] += 1
    grid[x][y-1] += 1
    grid[x][y+1] += 1
    grid[x+1][y-1] += 1
    grid[x+1][y] += 1
    grid[x+1][y+1] += 1
    return
    




file = open("input.txt")

grid = np.zeros((12,12))

for i in range(12):
    grid[0][i] = -10000000
    grid[i][0] = -10000000
    grid[11][i] = -10000000
    grid[i][11] = -10000000

y = 1
for line in file:
    x = 1
    for char in line:
        if char != "\n":
            grid[x][y] = int(char)
            x += 1
    y += 1

flashCount = 0
for _ in range(100):
    grid += 1
    if 10 in grid:
        flashCount += flash(grid)

print(flashCount)