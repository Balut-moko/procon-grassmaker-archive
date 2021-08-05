from sys import stdin
from collections import Counter

readline = stdin.readline
n, k = map(int, readline().split())
a = Counter(map(int, readline().split())).most_common()
ans = 0
tmp = len(a)
i = 0
while k < tmp:
    i += 1
    ans += a[-i][1]
    tmp -= 1
print(ans)
