from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
q = int(readline())
di = defaultdict(int)
ele = -1
for _ in range(q):
    t, *x = map(int, readline().split())

    if t == 1:
        ele = x[0]
        di.clear()
    if t == 2:
        di[x[0] - 1] += x[1]
    if t == 3:
        if ele == -1:
            ans = a[x[0] - 1] + di[x[0] - 1]
        else:
            ans = ele + di[x[0] - 1]
        print(ans)
