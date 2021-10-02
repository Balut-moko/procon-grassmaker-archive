from sys import stdin
from itertools import product


def listtomaxint(li):
    li = sorted(li, reverse=True)
    res = ''
    for v in li:
        res += str(v)
    if res == '':
        res = 0
    return int(res)


readline = stdin.readline
n = list(map(int, readline()[:-1]))
digit = len(n)
ans = 0
for i in range(2**digit):
    a = []
    b = []
    for j in range(digit):
        if ((i >> j) & 1):
            a.append(n[j])
        else:
            b.append(n[j])
    ans = max(ans, listtomaxint(a) * listtomaxint(b))
print(ans)
