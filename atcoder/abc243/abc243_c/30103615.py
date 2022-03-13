from sys import stdin
from collections import defaultdict

readline = stdin.readline
n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in [0] * n]
s = readline()[:-1]

ans = "No"
xys = [(xy[0], xy[1], val) for xy, val in zip(xy, s)]
point_di = defaultdict(list)
for x, y, s in xys:
    point_di[y].append([x, s])
for li in point_di.values():
    li.sort()
    flg = False
    for val in li:
        if val[1] == "R":
            flg = True
        if flg:
            if val[1] == "L":
                ans = "Yes"
print(ans)
