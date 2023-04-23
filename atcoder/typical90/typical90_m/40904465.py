from heapq import heappop, heappush
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, readline().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(i):
    INF = 1 << 60
    dist = [INF] * len(graph)

    start = i
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        c, v = heappop(hq)
        if dist[v] < c:
            continue
        for to, cost in graph[v]:
            if dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


dist = dijkstra(0)
dist_n = dijkstra(n - 1)

for i in range(n):
    print(dist[i] + dist_n[i])
