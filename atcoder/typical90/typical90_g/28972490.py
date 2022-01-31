from sys import stdin
from bisect import bisect_left

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a.sort()
q = int(readline())
b = [int(readline()) for _ in [0] * q]
ans = [None] * q
for i, v in enumerate(b):
    idx = bisect_left(a, v)
    if idx == 0:
        ans[i] = abs(a[idx] - v)
    elif idx == n:
        ans[i] = abs(a[idx - 1] - v)
    else:
        ans[i] = min(abs(a[idx] - v), abs(a[idx - 1] - v))
print(*ans, sep="\n")
