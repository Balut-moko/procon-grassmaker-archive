from sys import stdin
from collections import deque


def bfs(grid):
    h = len(grid)
    w = len(grid[0])
    dist = [[1 << 60] * w for _ in range(h)]
    dist[0][0] = 0
    if grid[0][0] == "#":
        dist[0][0] = 1
    dd = ((1, 0), (0, 1))
    que = deque([(0, 0)])
    while que:
        r, c = que.popleft()
        cur = dist[r][c]
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if grid[r][c] == "." and grid[nr][nc] == "#":
                if cur + 1 < dist[nr][nc]:
                    dist[nr][nc] = cur + 1
                    que.append((nr, nc))
            else:
                if cur < dist[nr][nc]:
                    dist[nr][nc] = cur
                    que.append((nr, nc))
    return dist


readline = stdin.readline
h, w = map(int, readline().split())
grid = [readline()[:-1] for _ in [0] * h]
dist = bfs(grid)
print(dist[-1][-1])
