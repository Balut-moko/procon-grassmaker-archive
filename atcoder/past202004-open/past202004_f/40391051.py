from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin

readline = stdin.readline
n = int(readline())

dic = defaultdict(list)

for _ in range(n):
    a, b = map(int, readline().split())
    dic[a - 1].append(b)

hq = []
ans = 0
for i in range(n):
    for b in dic[i]:
        heappush(hq, -b)
    ans += -heappop(hq)
    print(ans)
