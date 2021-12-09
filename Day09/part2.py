

cave = [[10] * 102]
lows = []
file = open("input.txt")

for line in file:
    newline = [10]
    for char in line:
        if char != '\n':
            newline.append(int(char))
    newline.append(10)
    cave.append(newline)
cave.append([10] * 102)
for y in range(1,len(cave)-1):
    for x in range(1,len(cave[y])-1):
        if cave[y][x] < cave[y-1][x] and cave[y][x] < cave[y+1][x] and cave[y][x] < cave[y][x - 1] and cave[y][x] < cave[y][x + 1]:
            lows.append((y,x))


sizes = []
for low in lows:
    size = 0
    stack = [low]
    while len(stack) != 0:
        y,x = stack.pop()
        if cave[y][x] != 9 and cave[y][x] != 10:
            cave[y][x] = 9
            size += 1
            stack.append((y-1,x))
            stack.append((y+1,x))
            stack.append((y,x-1))
            stack.append((y,x+1))
    sizes.append(size)
sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])