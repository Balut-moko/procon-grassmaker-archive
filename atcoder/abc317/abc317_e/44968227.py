from collections import deque
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [readline()[:-1] for _ in [0] * h]

grid = [["."] * w for _ in range(h)]

for i in range(h):
    flag = False
    for j in range(w):
        if a[i][j] == "S":
            S = (i, j)
        if a[i][j] == "G":
            G = (i, j)
        if a[i][j] == "#":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == ".":
            if flag:
                grid[i][j] = "#"
        if a[i][j] == ">":
            grid[i][j] = "#"
            flag = True
        if a[i][j] == "<":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == "^":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == "v":
            grid[i][j] = "#"
            flag = False

for i in range(h):
    flag = False
    for j in range(w - 1, -1, -1):
        if a[i][j] == "#":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == ".":
            if flag:
                grid[i][j] = "#"
        if a[i][j] == ">":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == "<":
            grid[i][j] = "#"
            flag = True
        if a[i][j] == "^":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == "v":
            grid[i][j] = "#"
            flag = False

for j in range(w):
    flag = False
    for i in range(h):
        if a[i][j] == "#":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == ".":
            if flag:
                grid[i][j] = "#"
        if a[i][j] == ">":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == "<":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == "^":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == "v":
            grid[i][j] = "#"
            flag = True

for j in range(w):
    flag = False
    for i in range(h - 1, -1, -1):
        if a[i][j] == "#":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == ".":
            if flag:
                grid[i][j] = "#"
        if a[i][j] == ">":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == "<":
            grid[i][j] = "#"
            flag = False
        if a[i][j] == "^":
            grid[i][j] = "#"
            flag = True
        if a[i][j] == "v":
            grid[i][j] = "#"
            flag = False


def bfs(s):
    si, sj = s
    dist = [[-1] * w for _ in range(h)]
    dist[si][sj] = 0
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    que = deque([(si, sj)])
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


dist = bfs(S)
gi, gj = G
print(dist[gi][gj])
