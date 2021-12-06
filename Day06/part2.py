import re
import numpy as np

file = open("input.txt")

curr = np.zeros(9)
for line in file:
    p = re.compile(r'\d+')
    nums = p.findall(line)
    for entry in nums:
        num = int(entry)
        curr[num] += 1

for day in range(1, 257):
    next = np.zeros(9)
    next[0] = curr[1]
    next[1] = curr[2]
    next[2] = curr[3]
    next[3] = curr[4]
    next[4] = curr[5]
    next[5] = curr[6]
    next[6] = curr[7] + curr[0]
    next[7] = curr[8]
    next[8] = curr[0]
    curr = next

print(int(np.sum(curr)))