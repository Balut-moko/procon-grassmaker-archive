from sys import stdin


def meguru_bisect(ok, ng):
    def solve(mid):
        if a + b * mid <= c * mid * d:
            return True
        else:
            return False

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


readline = stdin.readline
a, b, c, d = map(int, readline().split())
ans = meguru_bisect(10**18, 0)
if ans == 10**18:
    ans = -1
print(ans)
