from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
c = [tuple(readline()[:-1]) for _ in [0] * h]
visited = [[False] * w for _ in range(h)]
dist = [[-1] * w for _ in range(h)]
nxt = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def dfs(i, j, cnt):
    if not(0 <= i < h and 0 <= j < w) or c[i][j] == "#":
        return -1
    visited[i][j] = True

    if dist[i][j] != -1:
        if cnt - dist[i][j] < 3:
            return -1
        return cnt - dist[i][j]

    res = -1
    dist[i][j] = cnt

    for nxt_i, nxt_j in nxt:
        nxt_i += i
        nxt_j += j
        res = max(res, dfs(nxt_i, nxt_j, cnt + 1))
    dist[i][j] = -1
    return res


ans = -1
for i in range(h):
    for j in range(w):
        if c[i][j] == ".":
            ans = max(ans, dfs(i, j, 0))
print(ans)
