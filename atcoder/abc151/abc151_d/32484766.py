from sys import stdin
from collections import deque


def bfs(grid, start):
    h = len(grid)
    w = len(grid[0])
    dist = [[-1] * w for _ in range(h)]
    dist[start[0]][start[1]] = 0
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    que = deque([start])
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


readline = stdin.readline
h, w = map(int, readline().split())
grid = [readline()[:-1] for _ in [0] * h]
ans = -1
for r in range(h):
    for c in range(w):
        if grid[r][c] == ".":
            start = (r, c)
            dist = bfs(grid, start)
            max_dist = max([max(row) for row in dist])
            ans = max(ans, max_dist)
print(ans)
