from bisect import bisect_left
from itertools import accumulate


n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

bb = list(accumulate(b, initial=0))

ans = 0
for i in range(n):
    idx = bisect_left(b, p - a[i])
    ans += a[i] * idx + bb[idx]
    ans += (m - idx) * p

print(ans)
