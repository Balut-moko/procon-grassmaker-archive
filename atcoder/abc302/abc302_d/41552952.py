from bisect import bisect_left, bisect_right
from sys import stdin

readline = stdin.readline
n, m, d = map(int, readline().split())
a = sorted(set(map(int, readline().split())))
b = sorted(set(map(int, readline().split())))
ans = -1
for val in a:
    l = bisect_left(b, val - d)
    r = bisect_right(b, val + d) - 1
    if l > r:
        continue
    ans = max(ans, val + b[r])
print(ans)