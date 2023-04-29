from itertools import product
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [tuple(readline()[:-1]) for _ in [0] * h]
b = [tuple(readline()[:-1]) for _ in [0] * h]

flag = False
for i, j in product(range(h + 1), range(w + 1)):
    aa = a[i:] + a[:i]
    aat = list(zip(*aa))
    aat = aat[j:] + aat[:j]
    aatt = list(zip(*aat))
    for ii, jj in product(range(h), range(w)):
        if aatt[ii][jj] == b[ii][jj]:
            continue
        break
    else:
        flag = True

print("Yes" if flag else "No")
