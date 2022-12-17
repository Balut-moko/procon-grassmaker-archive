from itertools import combinations
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]
ans = 0

for i, j in combinations(range(n), 2):
    for k in range(m):
        if s[i][k] == "x" and s[j][k] == "x":
            break
    else:
        ans += 1
print(ans)
