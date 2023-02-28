from collections import deque
from heapq import heappop, heappush
from sys import stdin

readline = stdin.readline
n, m, x, y = map(int, readline().split())
x -= 1
y -= 1
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, t, k = map(int, readline().split())
    graph[a - 1].append((b - 1, t, k))
    graph[b - 1].append((a - 1, t, k))


def dijkstra():
    inf = 1 << 60
    dist = [inf] * len(graph)
    hq = [(0, x)]
    dist[x] = 0
    while hq:
        c, v = heappop(hq)
        if dist[v] < c:
            continue
        for to, t, k in graph[v]:
            cost = (k - (dist[v] + k) % k) % k + t
            if dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


dist = dijkstra()

print(dist[y] if dist[y] != 1 << 60 else -1)
