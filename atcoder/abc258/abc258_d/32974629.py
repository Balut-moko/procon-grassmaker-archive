from itertools import accumulate
from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

first = [a + b for a, b in ab]
first_cumsum = list(accumulate(first))

ans = 1 << 60

for i in range(n):
    tmp = first_cumsum[i]
    xx = x - i - 1
    if xx < 0:
        continue
    tmp += ab[i][1] * xx
    ans = min(ans, tmp)
print(ans)
