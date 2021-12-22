cost = [[int(point) for point in line] for line in open("input.txt").read().strip('\n\n').split('\n')]

maxDim = len(cost) - 1
start = (0, 0)
end = (maxDim, maxDim)
queue = []
bestPath = {start : ([start], 0)}

newPoint = (1, 0)
queue.append(([newPoint, start], cost[newPoint[0]][newPoint[1]]))  
bestPath[newPoint] = ([newPoint, start], cost[newPoint[0]][newPoint[1]])
newPoint = (0, 1)
queue.append(([newPoint, start], cost[newPoint[0]][newPoint[1]]) )
bestPath[newPoint] = ([newPoint, start], cost[newPoint[0]][newPoint[1]])

while(len(queue) > 0):
    cur = queue[0]
    queue = queue[1:]
    curPath = cur[0]
    curCost = cur[1]
    curX = curPath[0][0]
    curY = curPath[0][1]
    if end == (curX, curY):
        if end in bestPath:
            if bestPath[end][1] > curCost:
                bestPath[end] = (curPath, curCost)
        else:
            bestPath[end] = (curPath, curCost)
    else:
        toAdd = [(curX - 1, curY), (curX + 1, curY), (curX, curY - 1), (curX, curY + 1)]
        for newPoint in toAdd:
            if min(newPoint[:]) >= 0 and max(newPoint[:]) <= maxDim:
                if newPoint in bestPath:
                    if curCost + cost[newPoint[0]][newPoint[1]] < bestPath[newPoint][1]:
                        bestPath[newPoint] = ([newPoint] + curPath, curCost + cost[newPoint[0]][newPoint[1]])
                        queue.append(([newPoint] + curPath, curCost + cost[newPoint[0]][newPoint[1]]))
                else:
                    bestPath[newPoint] = ([newPoint] + curPath, curCost + cost[newPoint[0]][newPoint[1]])
                    queue.append(([newPoint] + curPath, curCost + cost[newPoint[0]][newPoint[1]]))

print(bestPath[end])
