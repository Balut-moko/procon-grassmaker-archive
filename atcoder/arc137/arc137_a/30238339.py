from sys import stdin
import math

readline = stdin.readline
l, r = map(int, readline().split())
ans = 1
for x in range(l, min(r, l + 1000)):
    for y in range(r, max(l, r - 1000), -1):
        if math.gcd(x, y) == 1:
            ans = max(ans, y - x)
print(ans)
