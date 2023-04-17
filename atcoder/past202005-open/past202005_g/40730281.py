from collections import deque
from sys import stdin

readline = stdin.readline
n, x, y = map(int, readline().split())

grid = [["."] * 410 for _ in [0] * 410]

for _ in range(n):
    xi, yi = map(int, readline().split())
    grid[yi + 205][xi + 205] = "#"


def bfs():
    h = len(grid)
    w = len(grid[0])
    dist = [[-1] * w for _ in range(h)]
    dist[205][205] = 0
    dd = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 0))
    que = deque([(205, 205)])
    while que:
        r, c = que.popleft()
        cur = dist[r][c]
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w) or grid[nr][nc] == "#":
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = cur + 1
                que.append((nr, nc))
    return dist


dist = bfs()
print(dist[y + 205][x + 205])
