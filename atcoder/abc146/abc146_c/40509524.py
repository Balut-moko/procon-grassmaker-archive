from sys import stdin

readline = stdin.readline
a, b, x = map(int, readline().split())


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        if a * mid + b * len(str(mid)) <= x:
            return True
        return False

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, 10 ** 9 + 1))
