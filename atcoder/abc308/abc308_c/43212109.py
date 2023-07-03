from sys import stdin
from functools import cmp_to_key


def cmp(x, y):
    a1, b1, i1 = x
    a2, b2, i2 = y
    calc = a1 * (a2 + b2) - a2 * (a1 + b1)
    if calc == 0:
        return 0
    return -1 if calc < 0 else 1


readline = stdin.readline
n = int(readline())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

lst = []

for i in range(n):
    a, b = ab[i]
    lst.append((a, b, -i))

lst.sort(reverse=True, key=cmp_to_key(cmp))

ans = []

for val in lst:
    a, b, i = val
    ans.append(-i + 1)

print(*ans)
