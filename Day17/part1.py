import re

desc = open("input.txt").read().strip()
target = (re.findall(r'[-+]?\d+', desc))
xTargetLeft = int(target[0])
xTargetRight = int(target[1])
yTargetBottom = int(target[2])
yTargetTop = int(target[3])

def run(xV, yV):
    yMax = 0

    xP = 0
    yP = 0

    while xP < xTargetRight and yP > yTargetBottom:
        xP += xV
        yP += yV 
        yMax = max(yP, yMax)

        if xV > 0:
            xV -= 1
        elif xV < 0:
            xV += 1
        
        yV -= 1

        if xTargetLeft <= xP and xP <= xTargetRight and yTargetBottom <= yP and yP <= yTargetTop:
            return yMax
    
    return -1


yMax = 0
for xV in range(100):
    for yV in range(1000):
        yMax = max(yMax, run(xV, yV))
print(yMax)