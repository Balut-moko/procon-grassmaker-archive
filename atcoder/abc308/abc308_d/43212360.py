from collections import deque
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * h]
snuke = "snukes"
if s[0][0] != "s":
    print("No")
    exit()


def bfs(grid):
    h = len(grid)
    w = len(grid[0])
    dist = [[-1] * w for _ in range(h)]
    dist[0][0] = 0
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    que = deque([(0, 0)])
    while que:
        r, c = que.popleft()
        cur = dist[r][c]
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if not (grid[nr][nc] == snuke[cur % 5 + 1]):
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = cur + 1
                que.append((nr, nc))
    return dist


dist = bfs(s)
print("Yes" if dist[-1][-1] > 0 else "No")
