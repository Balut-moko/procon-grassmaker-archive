from collections import deque
from sys import stdin

readline = stdin.readline
n1, n2, m = map(int, readline().split())

graph = [[] for _ in range(n1 + n2)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(s):
    dist = [-1] * len(graph)
    que = deque([s])  # root
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in graph[v]:
            if dist[w] != -1:
                continue
            dist[w] = d + 1
            que.append(w)
    return dist


dist_0 = bfs(0)
dist_nn = bfs(n1 + n2 - 1)

print(max(dist_0) + max(dist_nn) + 1)
