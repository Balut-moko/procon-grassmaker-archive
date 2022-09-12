import math
from sys import stdin


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
g = 0
for i in range(1, n):
    g = math.gcd(g, abs(a[i - 1] - a[i]))
if g == 1:
    ans = 2
else:
    ans = 1
print(ans)
