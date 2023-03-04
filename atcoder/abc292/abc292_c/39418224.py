from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
di = defaultdict(int)
for i in range(1, n):
    for j in range(1, n):
        if i *j > n:
            break
        di[i * j] += 1

ans = 0
vals = list(di.items())
for num, val in vals:
    ans += val * di[n - num]

print(ans)
