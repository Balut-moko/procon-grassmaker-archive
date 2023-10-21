from heapq import heappop, heappush


N, A, B, C = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in [0] * N]

graph = [[] for _ in range(2 * N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        car = D[i][j] * A
        train = D[i][j] * B + C
        graph[i].append((j, car))
        graph[i].append((j + N, train))
        graph[i + N].append((j + N, train))


def dijkstra():
    INF = 1 << 60
    dist = [INF] * len(graph)

    start = 0
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


dist = dijkstra()

ans = min(dist[N - 1], dist[2 * N - 1])
print(ans)
