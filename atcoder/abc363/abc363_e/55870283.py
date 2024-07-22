from collections import Counter
from heapq import heappop, heappush


def grid2graph(grid, init_index=0):
    h = len(grid)
    w = len(grid[0])

    def idx(r, c):
        return r * w + c + init_index

    graph = [[] for _ in range(h * w + init_index)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "#":
                continue
            dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
            for dr, dc in dd:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < h and 0 <= nc < w) or grid[nr][nc] == "#":
                    continue
                graph[idx(r, c)].append((idx(nr, nc), AA[nr][nc]))
    return graph


H, W, Y = map(int, input().split())

A = [tuple(map(int, input().split())) for _ in [0] * H]

AA = []
AA.append(tuple([0] * (W + 2)))
for a in A:
    AA.append(tuple([0] + list(a) + [0]))
AA.append(tuple([0] * (W + 2)))

graph = grid2graph(AA)

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
        if max(dist[v], cost) < dist[to]:
            dist[to] = max(dist[v], cost)
            heappush(hq, (dist[to], to))

cnt = Counter(dist)

ans = H * W

for i in range(1, Y + 1):
    ans -= cnt[i]
    print(ans)
