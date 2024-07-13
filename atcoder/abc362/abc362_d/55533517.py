from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for i in range(M):
    u, v, cost = map(int, input().split())
    graph[u - 1].append((v - 1, cost))
    graph[v - 1].append((u - 1, cost))


def dijkstra():
    INF = 1 << 60
    dist = [INF] * len(graph)

    start = 0
    hq = [(A[0], start)]
    dist[start] = A[0]
    while hq:
        c, v = heappop(hq)
        if dist[v] < c:
            continue
        for to, cost in graph[v]:
            if dist[v] + cost + A[to] < dist[to]:
                dist[to] = dist[v] + cost + A[to]
                heappush(hq, (dist[to], to))
    return dist


dist = dijkstra()

print(*dist[1:])
