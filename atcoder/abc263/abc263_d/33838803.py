from itertools import accumulate
from sys import stdin

readline = stdin.readline
n, l, r = map(int, readline().split())
a = list(map(int, readline().split()))
ar = [r - val for val in a]
cum_a = [0] + list(accumulate(a))
cum_ar = [0] + list(accumulate(ar[::-1]))
cum_ar_idx = list(range(n + 1))
tmp = cum_ar[0]
for i in range(1, n + 1):
    if cum_ar[i] < tmp:
        cum_ar_idx[i] = i
        tmp = cum_ar[i]
    else:
        cum_ar_idx[i] = cum_ar_idx[i - 1]
ans = 1 << 60
for x in range(n + 1):
    y = cum_ar_idx[n - x]
    tmp = l * x - cum_a[x] + cum_a[n - y] + r * y
    ans = min(ans, tmp)

print(ans)
