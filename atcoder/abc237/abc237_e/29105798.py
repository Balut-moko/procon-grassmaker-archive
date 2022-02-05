from sys import stdin
from heapq import heappop, heappush


def dijkstra(graph, start, n):
    inf = 1 << 60
    dist = [inf] * n
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        v = heappop(hq)[1]
        for to, cost in graph[v]:
            if dist != inf and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    dist = [val if val != inf else -1 for val in dist]
    return dist


readline = stdin.readline
n, m = map(int, readline().split())
h = list(map(int, readline().split()))
graph = [[] for _ in range(n)]
ans = -1 << 60
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    if h[a] >= h[b]:
        graph[a].append([b, 0])
        graph[b].append([a, h[a] - h[b]])
    else:
        graph[a].append([b, h[b] - h[a]])
        graph[b].append([a, 0])

ans = dijkstra(graph, 0, n)
ans = [h[0] - h[i] - ans[i] for i in range(n)]
print(max(ans))
