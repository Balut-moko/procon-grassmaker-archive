from sys import stdin


def round_up0(p, q):
    if q < 0:
        p = -p
        q = -q
    return (p + q - 1) // q


readline = stdin.readline
n, a, b = map(int, readline().split())
an = list(map(int, readline().split()))


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        x = 0
        y = 0
        for val in an:
            if val < mid:
                x += round_up0(mid - val, a)
            else:
                y += (val - mid) // b
        if x <= y:
            return True
        return False

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(-1, 10 ** 18))
