from collections import deque
from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * n]

graph = [[] for _ in range(n * 2)]
for i in range(n):
    for j in range(n):
        if a[i][j]:
            graph[i].append(j)
            graph[i].append(j + n)
            graph[i + n].append(j)
            graph[i + n].append(j + n)


def bfs(i):
    dist = [-1] * len(graph)
    que = deque([i])  # root
    dist[i] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in graph[v]:
            if dist[w] != -1:
                continue
            dist[w] = d + 1
            que.append(w)
    return dist


Q = int(readline())
for _ in range(Q):
    s, t = map(lambda x: int(x) - 1, readline().split())
    dist = bfs(s % n)
    if s // n == t // n:
        print(dist[t % n])
    else:
        t = t % n + n
        print(dist[t])
