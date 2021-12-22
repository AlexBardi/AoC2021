from collections import Counter 
file = open("input.txt")

base = ""
rules = {}
first = True

for line in file:
    if first:
        base = line[:-1]
        first = False
    elif line != '\n':
        rules[line[0:2]] = line[6]

for _ in range(10):
    newBase = ""
    for i in range(len(base)-1):
        pair = base[i:i+2]
        if pair in rules:
            newBase += base[i] + rules[pair]
        else:
            newBase += base[i]
    newBase += base[-1]
    base = newBase

charCount = Counter(base)
maxi = max(charCount.values())
mini = min(charCount.values())

print(maxi - mini)  # 2375


