from sys import stdin
from itertools import accumulate
readline = stdin.readline
n, q = map(int, readline().split())
a = list(map(int, readline().split()))
c = list(map(int, readline().split())) + [1]
mod = 10**9 + 7
path = [pow(a[i], a[i + 1], mod) for i in range(n - 1)]
cs_path = [0] + list(accumulate(path))
pre = 0
ans = 0
for i in range(q + 1):
    nxt = c[i] - 1
    ans += abs(cs_path[pre] - cs_path[nxt])
    ans %= mod
    pre = nxt
print(ans)
