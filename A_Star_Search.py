import math
import heapq

class Node_state:
    def __init__(self, node, g, h, parent=None):
        self.node = node
        self.g = g
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def heuristic(coordinates, node, goal):
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def A_STAR_SEARCH(coordinates, adjlist, start, goal):
    minPq = []
    startnodeheuristic = heuristic(coordinates, start, goal)
    startnodestate = Node_state(start, 0, startnodeheuristic)

    best_g = {start: 0}
    bestpath = None
    bestcost = float('inf')

    heapq.heappush(minPq, startnodestate)

    while minPq:
        currentstate = heapq.heappop(minPq)
        if currentstate.g > best_g[currentstate.node]:
            continue

        if currentstate.node == goal:
            if currentstate.g < bestcost:
                bestcost = currentstate.g
                path = []
                tempstate = currentstate

                while tempstate:
                    path.append(tempstate.node)
                    tempstate = tempstate.parent
                path.reverse()
                bestpath = path
            continue

        for neighbor, edgecost in adjlist[currentstate.node]:
            new_g = currentstate.g + edgecost
            if neighbor not in best_g or new_g < best_g[neighbor]:
                best_g[neighbor] = new_g
                h = heuristic(coordinates, neighbor, goal)
                f = new_g + h
                nextstate = Node_state(neighbor, new_g, f, currentstate)
                heapq.heappush(minPq, nextstate)

    return (bestpath, bestcost) if bestpath else (None, -1)

coordinates = {
    'S': (1, 2),
    'A': (2, 2),
    'G': (4, 5)
}

adjlist = {
    'S': [('A', 1), ('G', 10)],
    'A': [('G', 1)]
}

start = 'S'
goal = 'G'

solutionpath, solutioncost = A_STAR_SEARCH(coordinates, adjlist, start, goal)

if solutionpath:
    print("Solution Path:", " -> ".join(solutionpath))
    print("Solution Cost:", solutioncost)
else:
    print("No path exists")
