from sys import stdin
from collections import defaultdict

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
mod = 998244353
di = defaultdict(set)
for i, val in enumerate(a):
    di[val].add(i)
if di[0] != {0}:
    print(0)
    exit()

ans = 1
before = 1
for i in range(1, n):
    ans *= pow(before, len(di[i]), mod)
    ans %= mod
    before = len(di[i])
print(ans)
