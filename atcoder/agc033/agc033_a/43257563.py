from collections import deque
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * h]

start = []
dist = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            start.append([i, j])
            dist[i][j] = 0


def bfs():
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    que = deque(start)
    while que:
        r, c = que.popleft()
        cur = dist[r][c]
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w) or s[nr][nc] == "#":
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = cur + 1
                que.append((nr, nc))


bfs()

ans = 0

for i in range(h):
    ans = max(ans, max(dist[i]))
print(ans)
