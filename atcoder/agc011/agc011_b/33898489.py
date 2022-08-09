from heapq import heappop, heappush
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a.sort()
cnt = 0
t = 0
for i in range(n - 1):
    cnt += a[i]
    if cnt * 2 < a[i + 1]:
        t = i + 1
print(n - t)
