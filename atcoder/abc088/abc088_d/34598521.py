from collections import deque
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
grid = [list(readline()[:-1]) for _ in [0] * h]


def bfs(grid):
    dist = [[-1] * w for _ in range(h)]
    dist[0][0] = 1
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    que = deque([(0, 0)])
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


dist = bfs(grid)
if dist[-1][-1] == -1:
    print(-1)
    exit()
ans = 0
for i in range(h):
    ans += grid[i].count(".")
ans -= dist[-1][-1]
print(ans)
