from collections import Counter
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

c = Counter(a)
ans = n * (n - 1) * (n - 2) // 6

for key, val in c.items():
    if val == 1:
        continue
    if val == 2:
        ans -= n - 2
    else:
        ans -= (val * (val - 1) // 2) * (n - val)
        ans -= val * (val - 1) * (val - 2) // 6
print(ans)
