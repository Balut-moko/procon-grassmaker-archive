from sys import stdin
from itertools import combinations
from typing import Tuple

readline = stdin.readline
n = int(readline())
a = [tuple(map(int, readline().split())) for _ in [0] * n]
ans = 0
for val in combinations(a, 2):
    l1, r1 = val[0][1], val[0][2]
    l2, r2 = val[1][1], val[1][2]
    if r1 < l2 or r2 < l1:
        continue
    ans += 1
    if l2 == r1 or l1 == r2:
        flg = False
        if l2 == r1:
            if (val[0][0] == 1 or val[0][0] == 3) and (val[1][0] == 1 or val[1][0] == 2):
                flg = True
        if l1 == r2:
            if (val[0][0] == 1 or val[0][0] == 2) and (val[1][0] == 1 or val[1][0] == 3):
                flg = True
        if not flg:
            ans -= 1
print(ans)
