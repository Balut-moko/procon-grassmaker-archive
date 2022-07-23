from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
di = defaultdict(int)

for _ in range(n):
    s = readline()[:-1]
    if di[s] == 0:
        print(s)
    else:
        print(f"{s}({di[s]})")
    di[s] += 1
