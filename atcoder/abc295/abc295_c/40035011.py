from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

di = defaultdict(int)

for val in a:
    di[val] += 1

ans = 0
for v in di.values():
    ans += v // 2

print(ans)
