from collections import defaultdict
from sys import stdin

readline = stdin.readline
h, w, n, hh, ww = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * h]

cnt = [[[0] * (n + 1) for _ in [0] * (w + 1)] for _ in [0] * (h + 1)]

for i in range(h):
    for j in range(w):
        for k in range(n + 1):
            cnt[i + 1][j + 1][k] = cnt[i][j + 1][k] + cnt[i + 1][j][k] - cnt[i][j][k]
            if k == a[i][j]:
                cnt[i + 1][j + 1][k] += 1

grid = [[None] * (w - ww + 1) for _ in range(h - hh + 1)]

for i in range(h - hh + 1):
    for j in range(w - ww + 1):
        tmp = 0
        ii = i + hh
        jj = j + ww
        for k in range(n + 1):
            if (
                cnt[h][w][k]
                - cnt[ii][jj][k]
                + cnt[ii][j][k]
                + cnt[i][jj][k]
                - cnt[i][j][k]
            ):
                tmp += 1
        grid[i][j] = tmp

for val in grid:
    print(*val)
