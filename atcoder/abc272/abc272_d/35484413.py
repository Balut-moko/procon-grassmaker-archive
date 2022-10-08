from math import sqrt
from sys import stdin
from collections import deque


def bfs(grid, dd):
    h = len(grid)
    w = len(grid[0])
    dist = [[-1] * w for _ in range(h)]
    dist[0][0] = 0
    que = deque([(0, 0)])
    while que:
        r, c = que.popleft()
        cur = dist[r][c]
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = cur + 1
                que.append((nr, nc))
    return dist


readline = stdin.readline
n, m = map(int, readline().split())

dd = set()

for i in range(m):
    jj = m - i * i
    if jj >= 0:
        j = int(sqrt(jj))
        if i * i + j * j == m:
            dd.add((i, j))
            dd.add((-i, j))
            dd.add((i, -j))
            dd.add((-i, -j))
            dd.add((j, i))
            dd.add((-j, i))
            dd.add((j, -i))
            dd.add((-j, -i))

grid = [[0] * n for _ in [0] * n]

dist = bfs(grid, dd)
for val in dist:
    print(*val)
