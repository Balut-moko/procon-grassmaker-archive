from itertools import product
from sys import stdin


def backtrace(s, now, cw, dist):
    r, c = now
    if now == s:
        if dist[r][c] != -1:
            return dist[r][c] + 1
        else:
            dist[r][c]
    res = -1
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    for dr, dc in dd:
        nr = r + dr
        nc = c + dc
        if not 0 <= nr < h or not 0 <= nc < w or cw[nr][nc] == "#":
            continue
        if dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            res = max(res, backtrace(s, (nr, nc), cw, dist))
    dist[r][c] = -1
    return res


readline = stdin.readline
h, w = map(int, readline().split())
cw = [tuple(readline()[:-1]) for _ in [0] * h]

ans = -1
for i, j in product(range(h), range(w)):
    if cw[i][j] != "#":
        s = (i, j)
        dist = [[-1] * w for _ in range(h)]
        ans = max(ans, backtrace(s, s, cw, dist))
if ans < 3:
    ans = -1
print(ans)
