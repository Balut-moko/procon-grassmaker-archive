from sys import stdin
from heapq import heappop, heappush
readline = stdin.readline
inf = 1 << 60


def dijkstra(graph, start, end, n):
    dist = [inf] * n
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        v = heappop(hq)[1]
        for to, cost in graph[v]:
            if dist != inf and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist[end] if dist[end] != inf else -1


n, k = map(int, readline().split())
graph = [[] for _ in range(n)]
for i in range(k):
    a, *b = map(int, readline().split())
    if a == 0:
        print(dijkstra(graph, b[0] - 1, b[1] - 1, n))
    else:
        graph[b[0] - 1].append((b[1] - 1, b[2]))
        graph[b[1] - 1].append((b[0] - 1, b[2]))
