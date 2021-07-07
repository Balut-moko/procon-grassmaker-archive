from sys import stdin
from operator import mul
from functools import reduce


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


readline = stdin.readline
n = int(readline())
s = readline()[:-1]
tmp = 0
ans = 0
if 1 < n:
    ans = combinations_count(n, 2)
for i in range(n):
    if s[tmp] == s[i]:
        continue
    else:
        if i - tmp != 1:
            ans -= combinations_count(i - tmp, 2)
        tmp = i
if 1 <= i - tmp:
    ans -= combinations_count(i - tmp + 1, 2)
print(ans)
