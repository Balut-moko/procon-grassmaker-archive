from collections import defaultdict
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * m]

di = defaultdict(int)

for i in range(m):
    for j in range(1, n):
        di[(a[i][j - 1], a[i][j])] += 1
        di[(a[i][j], a[i][j - 1])] += 1

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if di[(i, j)] == 0:
            ans += 1
print(ans)
