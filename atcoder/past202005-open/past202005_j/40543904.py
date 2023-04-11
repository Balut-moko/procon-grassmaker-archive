from bisect import bisect_right
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
child = [0] * n
for val in a:
    idx = bisect_right(a, -val)
    if idx == n:
        print(-1)
        continue
    a[idx] = -val
    print(idx + 1)
