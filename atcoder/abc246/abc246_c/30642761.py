from sys import stdin
from heapq import heapify, heappop, heappush


readline = stdin.readline
n, k, x = map(int, readline().split())
a = list(map(lambda x: -int(x), readline().split()))
heapify(a)

while k > 0:
    tmp = -heappop(a)
    if tmp == 0:
        break
    if tmp - x < 0:
        k -= 1
        tmp = 0
    else:
        div, mod = divmod(tmp, x)
        if div <= k:
            k -= div
            tmp = mod
        else:
            tmp -= k * x
            k = 0
    heappush(a, -tmp)

print(-sum(a))
