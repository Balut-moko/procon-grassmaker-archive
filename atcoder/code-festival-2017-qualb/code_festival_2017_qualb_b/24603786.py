from sys import stdin
from collections import Counter
readline = stdin.readline
n = int(readline())
d = Counter(map(int, readline().split()))
m = int(readline())
t = Counter(map(int, readline().split()))
ans = 'YES'
for key, val in t.items():
    if d[key] < val:
        ans = 'NO'
print(ans)
