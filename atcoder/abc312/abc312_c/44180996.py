from bisect import bisect_right
from sys import stdin


readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
a.sort()
c = a + b
c.sort()
for i in range(m):
    b[i] *= -1
b.sort()

for x in c:
    seller = bisect_right(a, x)
    buyer = bisect_right(b, -x)
    if seller >= buyer:
        print(x)
        exit()
    seller = bisect_right(a, x + 1)
    buyer = bisect_right(b, -x - 1)
    if seller >= buyer:
        print(x + 1)
        exit()
