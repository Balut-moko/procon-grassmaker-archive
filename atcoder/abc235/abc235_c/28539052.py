from sys import stdin
from collections import defaultdict
readline = stdin.readline
n, q = map(int, readline().split())
a = list(map(int, readline().split()))
xk = [tuple(map(int, readline().split())) for _ in [0] * q]

val_dict = defaultdict(list)
for i in range(n):
    val_dict[a[i]].append(i + 1)

for x, k in xk:
    if len(val_dict[x]) >= k:
        print(val_dict[x][k - 1])
    else:
        print(-1)
