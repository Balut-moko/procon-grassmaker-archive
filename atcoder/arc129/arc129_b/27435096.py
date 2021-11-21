from sys import stdin
from math import ceil

readline = stdin.readline
n = int(readline())
lr = [tuple(map(int, readline().split())) for _ in [0] * n]
max_l, min_r = lr[0][0], lr[0][1]
for i in range(n):
    max_l = max(max_l, lr[i][0])
    min_r = min(min_r, lr[i][1])
    if max_l <= min_r:
        ans = 0
    else:
        ans = ceil((max_l - min_r) / 2)
    print(ans)
