from sys import stdin
from collections import deque

readline = stdin.readline
n = int(readline())
ax, ay = map(lambda x: int(x) - 1, readline().split())
bx, by = map(lambda x: int(x) - 1, readline().split())
grid = [tuple(readline()[:-1]) for _ in [0] * n]

dist = [[[1 << 60] * 4 for _ in range(n)] for _ in range(n)]
dd = ((-1, -1), (1, -1), (-1, 1), (1, 1))
que = deque()
for i in range(4):
    dr, dc = dd[i]
    nr = ax + dr
    nc = ay + dc
    if not 0 <= nr < n or not 0 <= nc < n or grid[nr][nc] == "#":
        continue
    dist[nr][nc][i] = 1
    que.appendleft((nr, nc, i))
while que:
    r, c, w = que.popleft()
    if r == bx and c == by:
        print(dist[r][c][w])
        exit()
    cur = dist[r][c][w]
    for i in range(4):
        dr, dc = dd[i]
        nr = r + dr
        nc = c + dc
        if not 0 <= nr < n or not 0 <= nc < n or grid[nr][nc] == "#":
            continue
        if w == i:
            if dist[nr][nc][i] > cur:
                dist[nr][nc][i] = cur
                que.appendleft((nr, nc, i))
        else:
            if dist[nr][nc][i] > cur + 1:
                dist[nr][nc][i] = cur + 1
                que.append((nr, nc, i))
print(-1)
