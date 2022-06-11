from bisect import bisect_right
from itertools import accumulate
from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())
a = list(map(int, readline().split()))
x_li = [int(readline()) for _ in [0] * q]
a.sort()

a_cumsum = [0] + list(accumulate(a))


for x in x_li:
    k = bisect_right(a, x)
    ans = x * k
    ans -= a_cumsum[k]
    ans += a_cumsum[n] - a_cumsum[k]
    ans -= x * (n - k)
    print(ans)
