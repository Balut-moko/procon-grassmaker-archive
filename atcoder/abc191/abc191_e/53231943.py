from heapq import heappop, heappush


def dijkstra(start):
    INF = 1 << 60
    dist = [INF] * len(graph)

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


N, M = map(int, input().split())

graph = [[] for _ in range(N)]
ans = [1 << 60] * N
for i in range(M):
    u, v, c = map(int, input().split())
    graph[u - 1].append((v - 1, c))
    if u == v:
        ans[u - 1] = min(ans[u - 1], c)

dists = []
for i in range(N):
    dists.append(dijkstra(i))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        ans[i] = min(ans[i], dists[i][j] + dists[j][i])

for i in range(N):
    if ans[i] == 1 << 60:
        ans[i] = -1
print(*ans, sep="\n")
