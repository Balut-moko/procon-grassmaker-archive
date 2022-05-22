from collections import defaultdict, Counter
from sys import stdin

readline = stdin.readline
n = int(readline())
s = [readline()[:-1] for _ in [0] * n]
di = defaultdict(list)

for i in range(n):
    for j in range(10):
        for val in "0123456789":
            if s[i][j] == val:
                di[val].append(j)
ans = 1 << 60
for num in "0123456789":
    c = Counter(di[num])
    tmp = 0
    for key, val in c.items():
        tmp = max(tmp, int(key) + (val - 1) * 10)
    ans = min(ans, tmp)
print(ans)
