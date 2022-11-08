from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
jaj = [j + 1 - a[j] for j in range(n)]
cnt = defaultdict(int)
for val in jaj:
    cnt[val] += 1
ans = 0
for i in range(n):
    ans += cnt[i + 1 + a[i]]
print(ans)
