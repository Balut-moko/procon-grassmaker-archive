from sys import stdin
from itertools import groupby

readline = stdin.readline
s = readline()[:-1]

sx = s.replace("25", "X")
ans = 0

for k, v in groupby(sx):
    if k == "X":
        c = len(list(v))
        ans += c * (c + 1) // 2
print(ans)
