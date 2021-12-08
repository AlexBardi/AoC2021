import numpy as np

file = open("input.txt")

crabs = []
for line in file:
    crabsStr = line.split(",")
    for crab in crabsStr:
        crabs.append(int(crab))
crabs = np.array(crabs)

target = np.median(crabs)
cost = 0

for crab in crabs:
    cost += abs(target - crab)

print(cost)