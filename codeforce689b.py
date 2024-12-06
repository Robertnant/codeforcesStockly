from collections import deque
from collections import defaultdict

n = int(input())
shortcuts = list(map(int, input().split()))

# Zero base shortcuts for simplicity.
shortcuts = [x - 1 for x in shortcuts]

# Create graph to represent intersections.
adjList = defaultdict(set)
    
# Link each adjacent intersections
for node in range(1, n):
    prevNode = node - 1
    adjList[prevNode].add(node)
    adjList[node].add(prevNode)

# Add shortcuts
for (node, nearestNode) in enumerate(shortcuts):
    if node != nearestNode:
        adjList[node].add(nearestNode)

# Perform bfs to get shortest time since graph has one-unit edges.
visited = [False] * n
startNode = 0
q = deque()
q.append((startNode, 0))    # to the right side
visited[startNode] = True

timePerNode = [0] * n
while len(q) != 0:
    node, time = q.popleft()    # from the right side
    timePerNode[node] = time

    for child in adjList[node]:
        if visited[child] == False:
            visited[child] = True
            q.append((child, time + 1)) # to the right side

for time in timePerNode:
    print(time, end=" ")
