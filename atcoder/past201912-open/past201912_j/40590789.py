from heapq import heappop, heappush
from itertools import product
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * h]


def grid_dijkstra(sr, sc):
    INF = 1 << 60
    dist = [[INF] * w for _ in range(h)]
    dist[sr][sc] = 0
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    hq = [(0, sr, sc)]

    while hq:
        d, r, c = heappop(hq)
        if dist[r][c] < d:
            continue
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if d + a[nr][nc] < dist[nr][nc]:
                dist[nr][nc] = d + a[nr][nc]
                heappush(hq, (dist[nr][nc], nr, nc))
    return dist


dist1 = grid_dijkstra(h - 1, 0)
dist2 = grid_dijkstra(h - 1, w - 1)
dist3 = grid_dijkstra(0, w - 1)
ans = 1 << 60
for i, j in product(range(h), range(w)):
    ans = min(ans, dist1[i][j] + dist2[i][j] + dist3[i][j] - a[i][j] * 2)
print(ans)
