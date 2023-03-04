from math import cos, radians, sin
from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
if a < b:
    a, b = b, a
p1 = (0, 0)


def calc_point(p2):
    r = radians(60)
    x = p2[0] * cos(r) - p2[1] * sin(r)
    y = p2[0] * sin(r) + p2[1] * cos(r)
    return (x, y)


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        if mid < a:
            p2 = (mid, 0)
        elif mid - a < b:
            p2 = (a, mid - a)
        else:
            return False
        p3 = calc_point(p2)

        if p3[0] <= a and p3[1] <= b:
            return True
        return False

    cnt = 500
    while cnt:
        mid = (ok + ng) / 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
        cnt -= 1
    return ok


p = meguru_bisect(0, 2000)
if p < a:
    ans = p
elif p - a < b:
    ans = (a * a + (p - a) * (p - a)) ** 0.5

print(ans)
