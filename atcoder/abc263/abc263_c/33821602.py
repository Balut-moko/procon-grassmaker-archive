from itertools import permutations
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
li = list(range(1, m + 1))
for val in permutations(li, n):
    for i in range(n - 1):
        if val[i] < val[i + 1]:
            continue
        break
    else:
        print(*val)
