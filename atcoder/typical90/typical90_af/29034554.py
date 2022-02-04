from sys import stdin
from itertools import permutations

readline = stdin.readline
n = int(readline())
a = [tuple(map(int, readline().split())) for _ in [0] * n]
m = int(readline())
xy = {tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * m}
ans = 1 << 60

for com in permutations(range(n)):
    tmp = 0
    for i in range(n):
        if i > 0:
            x, y = com[i - 1], com[i]
            if x > y:
                x, y = y, x
            if (x, y) in xy:
                break
        tmp += a[com[i]][i]
    else:
        ans = min(ans, tmp)
print(ans if ans != 1 << 60 else -1)
