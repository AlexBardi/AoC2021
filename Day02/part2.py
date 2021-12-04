file = open("input.txt")

aim = 0
horiz = 0
depth = 0

for line in file:
    elems = line.split()
    if elems[0] == "forward":
        horiz += int(elems[1])
        depth += aim * int(elems[1])
    elif elems[0] == "down":
        aim += int(elems[1])
    else:
        aim -= int(elems[1])

print(depth*horiz)
