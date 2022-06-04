from sys import stdin
from collections import deque


def bfs(graph, x, k):
    que = deque([[x, 0]])  # root
    dist = {x}
    while que:
        v, d = que.popleft()
        if d == k:
            continue
        for w in graph[v]:
            dist.add(w)
            que.append([w, d + 1])
    return sum(dist)


readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(readline())
for i in range(q):
    x, k = map(int, readline().split())
    print(bfs(graph, x, k))
