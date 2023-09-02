from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

dl = defaultdict(int)
dr = defaultdict(int)

dl[a[0]] = 1
for i in range(2, n):
    dr[a[i]] += 1
ans = 0
cs = 0
if a[0] != a[1]:
    ans = dl[a[0]] * dr[a[0]]
    cs = dl[a[0]] * dr[a[0]]
for j in range(2, n - 1):
    dl[a[j - 1]] += 1
    cs += dl[a[j - 1]] * dr[a[j - 1]]
    cs -= dl[a[j]] * dr[a[j]]
    ans += cs
    dr[a[j]] -= 1

print(ans)
