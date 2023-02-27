from sys import stdin
from itertools import groupby

readline = stdin.readline
t = int(readline())

for _ in range(t):
    n = int(readline())
    s = readline()[:-1]
    cnt = s.count("1")
    if cnt & 1:
        print(-1)
        continue
    cnt11 = s.count("11")

    if cnt >= 4 or cnt == 0 or not cnt11:
        print(cnt // 2)
        continue
    if n == 3:
        print(-1)
        continue
    if s == "0110":
        print(3)
        continue
    print(2)
