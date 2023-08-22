from itertools import product
from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
d = list(map(int, readline().split()))
nd = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
for val in d:
    nd.discard(val)

ans = 1 << 60
for val in product(nd, repeat=len(str(n))):
    if val[0] == 0:
        continue
    tmp = int("".join(list(map(str, val))))
    if n <= tmp:
        ans = min(ans, tmp)
for val in product(nd, repeat=len(str(n)) + 1):
    if val[0] == 0:
        continue
    tmp = int("".join(list(map(str, val))))
    if n <= tmp:
        ans = min(ans, tmp)

print(ans)
