from sys import stdin
from itertools import accumulate
from collections import defaultdict

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
s = list(accumulate(a, initial=0))
mp = defaultdict(int)
ans = 0
for r in range(n):
    mp[s[r]] += 1
    ans += mp[s[r + 1] - k]
print(ans)
