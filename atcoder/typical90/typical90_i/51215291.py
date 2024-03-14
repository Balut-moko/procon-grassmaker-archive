from bisect import bisect_left
from math import atan2, pi


def f(r1, r2):
    x1, y1 = r1
    x2, y2 = r2
    return x2 * y1 - y2 * x1


def g(p1, p2):
    r1, s1 = p1
    r2, s2 = p2
    return f(r1, r2)


N = int(input())
A = [tuple(map(int, input().split())) for _ in [0] * N]

ans = 0
for a in A:
    xa, ya = a
    AA = [(b[0] - xa, b[1] - ya) for b in A if a != b]
    degrees = [atan2(y, x) * 180 / pi for x, y in AA]
    degrees.sort()
    for d1 in degrees:
        idx = bisect_left(degrees, (d1 + 180) % 360) % (N - 1)
        d2 = degrees[idx]
        tmp = min(abs(d1 - d2), 360 - abs(d1 - d2))
        ans = max(ans, tmp)
        d2 = degrees[(idx - 1 + N - 1) % (N - 1)]
        tmp = min(abs(d1 - d2), 360 - abs(d1 - d2))
        ans = max(ans, tmp)

print(ans)
