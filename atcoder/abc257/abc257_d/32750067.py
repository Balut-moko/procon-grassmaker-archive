from sys import stdin
from heapq import heappop, heappush


def round_up0(p, q):
    if q < 0:
        p = -p
        q = -q
    return (p + q - 1) // q


def dijkstra(graph, start):
    inf = 1 << 60
    dist = [inf] * len(graph)
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        c, v = heappop(hq)
        if dist[v] < c:
            continue
        for to, cost in graph[v]:
            if max(cost, dist[v]) < dist[to]:
                dist[to] = max(cost, dist[v])
                heappush(hq, (dist[to], to))
    return max(dist)


readline = stdin.readline
n = int(readline())
xyp = [tuple(map(int, readline().split())) for _ in [0] * n]

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dist = abs(xyp[i][0] - xyp[j][0]) + abs(xyp[i][1] - xyp[j][1])
        cost = round_up0(dist, xyp[i][2])
        graph[i].append((j, cost))

ans = 1 << 60
for i in range(n):
    tmp = dijkstra(graph, i)
    ans = min(ans, tmp)
print(ans)
