from sys import stdin

readline = stdin.readline
R, B = map(int, readline().split())
x, y = map(int, readline().split())


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        r = R - mid
        b = B - mid
        if r < 0 or b < 0:
            return False
        z = r // (x - 1) + b // (y - 1)
        if mid <= z:
            return True
        return False

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, 10 ** 18 + 1))
