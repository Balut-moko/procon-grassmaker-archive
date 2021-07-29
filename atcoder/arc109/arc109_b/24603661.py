from sys import stdin

readline = stdin.readline
n = int(readline())


def meguru_bisect(ng, ok):
    def check(mid):
        if mid * (mid + 1) // 2 <= n + 1:
            return True
        return False
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(n - meguru_bisect(10**18, 0) + 1)
