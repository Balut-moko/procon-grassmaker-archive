from sys import stdin
from collections import Counter
readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
c = list(map(int, readline().split()))
a = Counter([x % 46 for x in a])
b = Counter([x % 46 for x in b])
c = Counter([x % 46 for x in c])
ans = 0
for i in a.keys():
    for j in b.keys():
        for k in c.keys():
            if (i + j + k) % 46 == 0:
                ans += a[i] * b[j] * c[k]
print(ans)
