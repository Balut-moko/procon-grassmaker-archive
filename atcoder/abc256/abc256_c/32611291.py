from itertools import product
from sys import stdin


readline = stdin.readline
hw = list(map(int, readline().split()))
ans = 0
for a, b, d, e in product(range(1, 29), range(1, 29), range(1, 29), range(1, 29)):
    c = hw[0] - a - b
    f = hw[1] - d - e
    g = hw[3] - a - d
    h = hw[4] - b - e
    i1 = hw[2] - g - h
    i2 = hw[5] - c - f
    if i1 == i2 and min(a, b, c, d, e, f, g, h, i1, i2) > 0:
        ans += 1
print(ans)
