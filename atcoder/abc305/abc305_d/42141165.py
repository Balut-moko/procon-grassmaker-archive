from bisect import bisect_left, bisect_right
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

cumsum = [0]
for i in range(1, n):
    if i % 2 == 1:
        cumsum.append(cumsum[-1])
    else:
        cumsum.append(cumsum[-1] + a[i] - a[i - 1])


Q = int(readline())
for _ in range(Q):
    l, r = map(int, readline().split())
    l_idx = bisect_right(a, l)
    r_idx = bisect_right(a, r) - 1
    ans = cumsum[r_idx] - cumsum[l_idx]
    if l_idx % 2 == 0:
        ans += a[l_idx] - l
    if r_idx % 2 == 1:
        ans += r - a[r_idx]
    print(ans)
