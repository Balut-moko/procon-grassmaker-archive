from sys import stdin
from collections import Counter

readline = stdin.readline
n, k = map(int, readline().split())
c = list(map(int, readline().split()))
kinds = Counter(c[:k])
ans = len(kinds)
for i in range(n - k):
    kinds[c[i + k]] += 1
    kinds[c[i]] -= 1
    if not kinds[c[i]]:
        del kinds[c[i]]
    ans = max(ans, len(kinds))
print(ans)
