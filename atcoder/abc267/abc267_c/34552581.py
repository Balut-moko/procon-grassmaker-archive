from itertools import accumulate
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
cs_a = [0] + list(accumulate(a))

ans = -1 << 60
tmp = 0
for i in range(m):
    tmp += (i + 1) * a[i]
ans = max(ans, tmp)

for i in range(1, n - m + 1):
    tmp -= cs_a[i + m - 1] - cs_a[i - 1]
    tmp += a[i + m - 1] * m
    ans = max(ans, tmp)
print(ans)
