from collections import deque
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    dist = [None] * len(graph)
    que = deque([0])  # root
    dist[0] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in graph[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + 1
            que.append(w)
    return dist


dist = bfs()

print("POSSIBLE" if dist[n - 1] and dist[n - 1] <= 2 else "IMPOSSIBLE")
