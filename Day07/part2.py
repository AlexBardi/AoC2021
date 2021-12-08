import numpy as np

def fuelCost(diff):
    return (diff / 2) * (diff + 1)

file = open("input.txt")

crabs = []
for line in file:
    crabsStr = line.split(",")
    for crab in crabsStr:
        crabs.append(int(crab))
crabs = np.array(crabs)

target = np.median(crabs)
cost = 0
costPlus = 0

for crab in crabs:
    cost += fuelCost(abs(target - crab))
    costPlus += fuelCost(abs((target + 1) - crab))

while costPlus < cost:
    target += 1   
    cost = 0
    costPlus = 0
    for crab in crabs:
        cost += fuelCost(abs(target - crab))
        costPlus += fuelCost(abs((target + 1) - crab))



print(cost)
print(target)
print(crabs.mean())


