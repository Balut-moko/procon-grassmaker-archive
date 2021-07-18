from sys import stdin
from itertools import combinations

readline = stdin.readline
a = list(map(int, readline().split()))
ans = 1 << 60
if 0 <= a[1] - (a[2] - a[1]) - a[0]:
    ans = min(ans, a[1] - (a[2] - a[1]) - a[0])
if 0 <= a[1] + (a[1] - a[0]) - a[2]:
    ans = min(ans, a[1] + (a[1] - a[0]) - a[2])
if (a[2] - a[0]) % 2 == 0:
    if 0 <= a[0] + ((a[2] - a[0]) // 2) - a[1]:
        ans = min(ans, a[0] + ((a[2] - a[0]) // 2) - a[1])
else:
    if 0 <= a[0] + ((a[2] - a[0]) // 2) - a[1]:
        ans = min(ans, a[0] + ((a[2] - a[0]) // 2) - a[1] + 2)
print(ans)
