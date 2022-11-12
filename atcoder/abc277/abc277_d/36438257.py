from collections import defaultdict
from sys import stdin
import copy

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
am = {val % m for val in a}
di = defaultdict(int)

for val in a:
    di[val % m] += val
ans = 0
pre = -10
tmp = 0
amam = sorted(am) + sorted(am)
for val in amam:
    if (pre + 1) % m == val:
        tmp += di[val]
    else:
        tmp = di[val]
    pre = val
    ans = max(ans, tmp)
print(max(sum(a) - ans, 0))
