cave = [[10] * 102]
totalRisk = 0
print(cave)
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
            totalRisk += cave[y][x] + 1

print(totalRisk)
        



