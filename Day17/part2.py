import re

desc = open("input.txt").read().strip()
target = (re.findall(r'[-+]?\d+', desc))
xTargetLeft = int(target[0])
xTargetRight = int(target[1])
yTargetBottom = int(target[2])
yTargetTop = int(target[3])

def run(xV, yV):
    xP = 0
    yP = 0

    while xP <= xTargetRight and yP >= yTargetBottom:
        xP += xV
        yP += yV 
        if xTargetLeft <= xP <= xTargetRight and yTargetBottom <= yP <= yTargetTop:
            return True

        if xV > 0:
            xV -= 1
        elif xV < 0:
            xV += 1
        
        yV -= 1

    
    return False


goodCount = 0
for xV in range(xTargetRight + 1):
    for yV in range(yTargetBottom, 1000):
        if run(xV, yV):
            goodCount += 1
print(goodCount)