from collections import Counter
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]
cnt = Counter(s)
ans = 0
for val in cnt.values():
    if val >= 2:
        ans += val * (val - 1) // 2
print(ans)
