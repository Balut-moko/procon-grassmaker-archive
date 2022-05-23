from sys import stdin
from heapq import heappop, heappush


def dijkstra(graph, start, n):
    inf = 1 << 60
    dist = [inf] * n
    hq = [(0, start)]
    dist[start] = 0
    prev = [-1] * n
    while hq:
        c, v = heappop(hq)
        if dist[v] < c:
            continue
        for to, cost, road in graph[v]:
            if dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                prev[to] = road
                heappush(hq, (dist[to], to))
    return prev


readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(lambda x: int(x) - 1, readline().split())
    graph[a].append((b, c + 1, i + 1))
    graph[b].append((a, c + 1, i + 1))

prev = dijkstra(graph, 0, n)

print(*prev[1:])
