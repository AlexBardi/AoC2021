file = open("input.txt")

depth = 0
distance = 0

for line in file:
    elems = line.split()
    if elems[0] == "forward":
        distance += int(elems[1])
    elif elems[0] == "down":
        depth += int(elems[1])
    else:
        depth-= int(elems[1])

print(depth*distance)