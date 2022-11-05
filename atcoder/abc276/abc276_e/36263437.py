from collections import deque
from itertools import combinations
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
grid = [tuple(readline()[:-1]) for _ in [0] * h]


def bfs(p1, p2):
    sr, sc = p1
    gr, gc = p2
    h = len(grid)
    w = len(grid[0])
    dist = [[-1] * w for _ in range(h)]
    dist[sr][sc] = 0
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    que = deque([p1])
    while que:
        r, c = que.popleft()
        cur = dist[r][c]
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w) or grid[nr][nc] != ".":
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = cur + 1
                que.append((nr, nc))
    return dist[gr][gc]


ans = -1
for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
            points = []
            for dr, dc in dd:
                nr = i + dr
                nc = j + dc
                if not (0 <= nr < h and 0 <= nc < w) or grid[nr][nc] != ".":
                    continue
                points.append((nr, nc))
            for p1, p2 in combinations(points, 2):
                ans = max(ans, bfs(p1, p2))

print("Yes" if ans != -1 else "No")
