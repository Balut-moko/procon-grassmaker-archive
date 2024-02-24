from heapq import heappop, heappush


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    l, d, k, c, A, B = map(int, input().split())
    graph[B - 1].append((A - 1, l, d, k, c))

INF = 1 << 60
dist = [-INF] * len(graph)

start = N - 1
hq = [(-INF, start)]
dist[start] = INF
while hq:
    t, v = heappop(hq)
    t = -t
    if t < dist[v]:
        continue
    for to, l, d, k, c in graph[v]:
        if l + c <= t:
            x = t - (l + c)
            nxt = l + min(k - 1, x // d) * d
            if dist[to] < nxt:
                dist[to] = nxt
                heappush(hq, (-dist[to], to))

for d in dist[:-1]:
    print(d if d != -INF else "Unreachable")
