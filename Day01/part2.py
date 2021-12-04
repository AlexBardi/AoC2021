file = open("input.txt")

inc = 0

prev = 100000000000
old = 100000000000
oldest = 100000000000

for line in file:
    curr = int(line)
    if curr+prev+old > prev+old+oldest:
        inc += 1
    oldest = old
    old = prev
    prev = curr

print(inc)
