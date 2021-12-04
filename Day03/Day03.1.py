file = open("input.txt")
import numpy as np

first = True

for line in file:
    if first:
        length = len(line) - 1
        oneCount=np.zeros(length)
        zipCount=np.zeros(length)
    for idx,digit in enumerate(line):
        if idx < length:
            if digit == "0":
                zipCount[idx] += 1
            else: # digit == 1
                oneCount[idx] += 1
    if first:
        print(zipCount)
        print(oneCount)
        print(line)
    first = False


gamma = ""
epsilon = ""

for idx in range(length):
    if oneCount[idx] > zipCount[idx]:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"

print(int(gamma,2)*int(epsilon,2))