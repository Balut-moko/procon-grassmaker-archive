from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
Q = int(readline())

row = [i + 1 for i in range(n)]
col = [i + 1 for i in range(n)]
rev = False

for _ in range(Q):
    t, *ab = map(int, readline().split())
    if t == 1:
        a, b = ab
        a -= 1
        b -= 1
        if rev:
            col[a], col[b] = col[b], col[a]
        else:
            row[a], row[b] = row[b], row[a]
    if t == 2:
        a, b = ab
        a -= 1
        b -= 1
        if rev:
            row[a], row[b] = row[b], row[a]
        else:
            col[a], col[b] = col[b], col[a]
    if t == 3:
        rev = not rev
    if t == 4:
        a, b = ab
        a -= 1
        b -= 1
        if rev:
            print(n * (row[b] - 1) + (col[a] - 1))
        else:
            print(n * (row[a] - 1) + (col[b] - 1))
