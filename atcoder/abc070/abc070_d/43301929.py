from collections import deque
from sys import stdin

readline = stdin.readline
n = int(readline())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    u, v, cost = map(int, readline().split())
    graph[u - 1].append((v - 1, cost))
    graph[v - 1].append((u - 1, cost))

q, k = map(int, readline().split())
k -= 1


def bfs():
    dist = [None] * len(graph)
    que = deque([k])  # root
    dist[k] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w, c in graph[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + c
            que.append(w)
    return dist


dist = bfs()

for _ in range(q):
    x, y = map(lambda x: int(x) - 1, readline().split())
    print(dist[x] + dist[y])
