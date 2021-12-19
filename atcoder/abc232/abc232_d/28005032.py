from sys import stdin
from collections import deque

readline = stdin.readline
h, w = map(int, readline().split())
grid = [tuple(readline()[:-1]) for _ in [0] * h]
dist = [[-1] * w for _ in range(h)]
dist[0][0] = 1
dd = ((1, 0), (0, 1))
que = deque([(0, 0)])

while que:
    r, c = que.popleft()
    cur = dist[r][c]
    for dr, dc in dd:
        nr = r + dr
        nc = c + dc
        if not 0 <= nr < h or not 0 <= nc < w or grid[nr][nc] == '#':
            continue
        if dist[nr][nc] == -1:
            dist[nr][nc] = cur + 1
            que.append((nr, nc))
print(max(list(map(lambda x: max(x), dist))))
