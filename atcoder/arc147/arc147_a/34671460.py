from heapq import heapify, heappop, heappush
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a_minus = [-val for val in a]
heapify(a_minus)
a_min = min(a)

ans = 0
while len(a_minus) > 1:
    a_max = -heappop(a_minus)
    tmp = a_max % a_min
    if tmp != 0:
        a_min = min(a_min, tmp)
        heappush(a_minus, -tmp)
    ans += 1
print(ans)
