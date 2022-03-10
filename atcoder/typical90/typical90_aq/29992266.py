from sys import stdin
from collections import deque


def bfs(grid, h, w, start, goal):
    dist = [[[10**6] * w for _ in range(h)] for _ in range(4)]
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    rs, cs = start
    rt, ct = goal
    que = deque([])
    for i in range(4):
        dist[i][rs][cs] = 0
        que.append((rs, cs, i))

    while que:
        r, c, pos = que.popleft()
        if r == rt and c == ct:
            break
        cur = dist[pos][r][c]
        for i in range(4):
            if cur + 1 < dist[i][r][c]:
                dist[i][r][c] = cur + 1
                que.append((r, c, i))

        dr, dc = dd[pos]
        nr = r + dr
        nc = c + dc
        if not 0 <= nr < h or not 0 <= nc < w or grid[nr][nc] == "#":
            continue
        if cur < dist[pos][nr][nc]:
            dist[pos][nr][nc] = cur
            que.appendleft((nr, nc, pos))
    return dist


readline = stdin.readline
h, w = map(int, readline().split())
start = list(map(lambda x: int(x) - 1, readline().split()))
goal = list(map(lambda x: int(x) - 1, readline().split()))
grid = [tuple(readline()[:-1]) for _ in [0] * h]

dist = bfs(grid, h, w, start, goal)
rt, ct = goal
ans = 10**6
for i in range(4):
    ans = min(ans, dist[i][rt][ct])
print(ans)
