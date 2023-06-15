from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))


def round_up0(p, q):
    if q < 0:
        p = -p
        q = -q
    return (p + q - 1) // q


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        cnt = 0
        for i in range(n):
            cnt += round_up0(a[i], mid) - 1
        return cnt <= k

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(10**10, 0))
