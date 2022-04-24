from sys import stdin
from collections import defaultdict

readline = stdin.readline
n, k = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]
ans = 0
for i in range(2**n):
    d = defaultdict(int)
    for j in range(n):
        if (i >> j) & 1:
            for val in s[j]:
                d[val] += 1
    cnt = 0
    for val in d.values():
        if val == k:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
