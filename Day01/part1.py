file = open("input.txt")

inc = 0
prev = 100000000000

for line in file:
    curr = int(line)
    if curr > prev:
        inc += 1
    prev = curr

print(inc)
