from sys import stdin
from itertools import accumulate

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
cs = list(accumulate(a))
cs = [c % 360 for c in cs]
cs.sort()
cut = [0] + cs + [360]

angle = max([cut[i] - cut[i - 1] for i in range(1, n + 2)])
print(angle)
