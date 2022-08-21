from bisect import bisect_left
from itertools import accumulate
from collections import deque
from sys import stdin

readline = stdin.readline
n, p, q, r = map(int, readline().split())
a = list(map(int, readline().split()))

cs_a = [0] + list(accumulate(a))


def check(x, y, z, w):
    if n < max(x, y, z, w):
        return False
    if cs_a[y] - cs_a[x] != p:
        return False
    if cs_a[z] - cs_a[y] != q:
        return False
    if cs_a[w] - cs_a[z] != r:
        return False
    return True


ans = "No"
for x in range(n):
    y = bisect_left(cs_a, p + cs_a[x])
    z = bisect_left(cs_a, p + q + cs_a[x])
    w = bisect_left(cs_a, p + q + r + cs_a[x])
    if check(x, y, z, w):
        ans = "Yes"
print(ans)
