import heapq

costOriginal = [[int(point) for point in line] for line in open("input.txt").read().strip('\n\n').split('\n')]
cost = [[0 for _ in range(500)] for _ in range(500)]

for i in range(100):
    for j in range(100):
        for k in range(5):
            for l in range(5):
                cost[i + (100 * k)][j + (100 * l)] = ((costOriginal[i][j] + k + l - 1) % 9) + 1

maxDim = len(cost) - 1
start = (0, 0)
end = (maxDim, maxDim)
queue = []
bestPath = {start: ([start], 0)}


def astar(point):
    x = point[0]
    y = point[1]
    return bestPath[(x, y)][1] + (maxDim - x) + (maxDim - y)

newPoint = (1, 0)
bestPath[newPoint] = ([newPoint, start], cost[newPoint[0]][newPoint[1]])
heapq.heappush(queue, (astar(newPoint), [newPoint, start], cost[newPoint[0]][newPoint[1]]))  # (queue, (astar, path, cost))
newPoint = (0, 1)
bestPath[newPoint] = ([newPoint, start], cost[newPoint[0]][newPoint[1]])
heapq.heappush(queue, (astar(newPoint), [newPoint, start], cost[newPoint[0]][newPoint[1]]))  # (queue, (astar, path, cost))

while not end in bestPath:
    cur = heapq.heappop(queue)
    curPath = cur[1]
    curCost = cur[2]
    curX = curPath[0][0]
    curY = curPath[0][1]
    if end == (curX, curY):
        if end in bestPath:
            if bestPath[end][1] > curCost:
                bestPath[end] = (curPath, curCost)
        else:
            bestPath[end] = (curPath, curCost)
    else:
        toAdd = [(curX - 1, curY), (curX + 1, curY),
                 (curX, curY - 1), (curX, curY + 1)]
        for newPoint in toAdd:
            if min(newPoint[:]) >= 0 and max(newPoint[:]) <= maxDim:
                if newPoint in bestPath:
                    if curCost + cost[newPoint[0]][newPoint[1]] < bestPath[newPoint][1]:
                        bestPath[newPoint] = ([newPoint] + curPath, curCost + cost[newPoint[0]][newPoint[1]])
                        heapq.heappush(queue, (astar(newPoint), [newPoint] + curPath, curCost + cost[newPoint[0]][newPoint[1]]))  # (queue, (astar, path, cost))
                else:
                    bestPath[newPoint] = ([newPoint] + curPath, curCost + cost[newPoint[0]][newPoint[1]])
                    heapq.heappush(queue, (astar(newPoint), [newPoint] + curPath, curCost + cost[newPoint[0]][newPoint[1]]))  # (queue, (astar, path, cost))
                    

print(bestPath[end])