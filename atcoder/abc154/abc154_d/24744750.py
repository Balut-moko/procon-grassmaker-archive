from sys import stdin
from itertools import accumulate

readline = stdin.readline
n, k = map(int, readline().split())
p = list(map(int, readline().split()))
p = [(val + 1) / 2 for val in p]
cumsum_p = [0] + list(accumulate(p))
ans = 0
for i in range(n - k + 1):
    ans = max(ans, cumsum_p[i + k] - cumsum_p[i])
print(ans)
