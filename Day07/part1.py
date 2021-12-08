import numpy as np

file = open("input.txt")

crabs = []
for line in file:
    crabsStr = line.split(",")
    for crab in crabsStr:
        crabs.append(int(crab))
crabs = np.array(crabs)

target = round(crabs.mean())
costsCur = 0
costsPrev = 0

for crab in crabs:
    costsCur += abs(crab - target)
    costsPrev += abs(crab - (target - 1))

while costsCur > costsPrev:
    target -= 1
    costsPrev = 0
    costsCur = 0
    for crab in crabs:
        costsCur += abs(crab - target)
        costsPrev += abs(crab - (target - 1))

print(costsCur)