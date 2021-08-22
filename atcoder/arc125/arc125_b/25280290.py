from sys import stdin
from bisect import bisect_left
readline = stdin.readline
n = int(readline())
mod = 998244353
ans = 0
sq_table = [i * i for i in range(10 * 6)]

for i in range(10**6 + 1):
    a1 = (i + 1) * (i + 1)
    sa = 2 * (i + 1)
    if 0 <= n - a1:
        tmp = (n - a1) // sa
        ans += tmp + 1
        ans %= mod
    else:
        break
print(ans)
