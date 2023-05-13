from sys import stdin
from collections import deque

readline = stdin.readline
h, w, t = map(int, readline().split())
grid = [tuple(readline()[:-1]) for _ in [0] * h]
dd = ((-1, 0), (0, 1), (1, 0), (0, -1))


def bfs(sr, sc):
    dist = [[1 << 60] * w for _ in range(h)]
    dist[sr][sc] = 0
    que = deque([(sr, sc)])
    while que:
        r, c = que.popleft()
        cur = dist[r][c]
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w) or grid[nr][nc] == "#":
                continue
            if dist[nr][nc] == 1 << 60:
                dist[nr][nc] = cur + 1
                que.append((nr, nc))
    return dist


okashi = []
for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            sr, sc = i, j
        if grid[i][j] == "G":
            gr, gc = i, j
        if grid[i][j] == "o":
            okashi.append((i, j))

cnt = len(okashi)

dist_lst = []
for i, j in okashi:
    dist = bfs(i, j)
    dist_lst.append(dist)


def has_bit(n, i):
    return n & (1 << i) > 0


ALL = 1 << (cnt)
dp = [[1 << 60] * cnt for _ in [0] * ALL]
for i in range(cnt):
    dp[1 << i][i] = dist_lst[i][sr][sc]

for n in range(1 << cnt):
    for i in range(cnt):
        if dp[n][i] == 1 << 60:
            continue
        for j in range(cnt):
            if has_bit(n, j):
                continue
            dp[n | 1 << j][j] = min(
                dp[n | 1 << j][j], dp[n][i] + dist_lst[i][okashi[j][0]][okashi[j][1]]
            )


ans = -1
dist = bfs(sr, sc)
if dist[gr][gc] <= t:
    ans = 0
for n in range(1 << cnt):
    for i in range(cnt):
        tmp = 0
        if dp[n][i] + dist_lst[i][gr][gc] <= t:
            for j in range(cnt):
                if has_bit(n, j):
                    tmp += 1
            ans = max(ans, tmp)

print(ans)
