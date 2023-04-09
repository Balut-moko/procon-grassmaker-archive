from itertools import product
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
s = [list(readline()[:-1]) for _ in [0] * h]

for i, j in product(range(h), range(w - 1)):
    if s[i][j] == "T" and s[i][j + 1] == "T":
        s[i][j] = "P"
        s[i][j + 1] = "C"

for val in s:
    print(*val, sep="")
