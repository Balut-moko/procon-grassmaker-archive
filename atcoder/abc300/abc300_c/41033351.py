from itertools import product
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
c = [tuple(readline()[:-1]) for _ in [0] * h]

s = [0] * min(h, w)


for i, j in product(range(1, h - 1), range(1, w - 1)):
    if c[i][j] == "#":
        if (
            c[i - 1][j - 1] == "#"
            and c[i - 1][j + 1] == "#"
            and c[i + 1][j + 1] == "#"
            and c[i + 1][j - 1] == "#"
        ):
            ii = i
            jj = j
            while c[ii][jj] == "#":
                ii += 1
                jj += 1
                if not (0 <= ii < h) or not (0 <= jj < w):
                    break
            size = ii - i - 2
            s[size] += 1

print(*s)
