file = open("input.txt")

diffCount = 0
for line in file:
    output = line.split()[-4:]
    for digit in output:
        if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
            diffCount += 1

print(diffCount)