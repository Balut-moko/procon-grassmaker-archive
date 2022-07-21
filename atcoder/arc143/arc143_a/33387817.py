from sys import stdin


def meguru_bisect(ok, ng):
    def solve(mid):
        if mid:
            return True
        return False

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


readline = stdin.readline
abc = list(map(int, readline().split()))
abc.sort()
a, b, c = abc
if 2 * c - a - b <= c:
    print(c)
else:
    print(-1)
