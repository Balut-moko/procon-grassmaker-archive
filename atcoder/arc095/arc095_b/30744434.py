from sys import stdin
from bisect import bisect_left


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a.sort()

cn = a[-1]
tmp = (cn + 1) // 2
cr_idx = bisect_left(a, tmp)
cr = a[cr_idx]
if cr_idx != 0:
    if abs(a[cr_idx - 1] - tmp) <= abs(cr - tmp):
        cr = a[cr_idx - 1]
print(cn, cr)
