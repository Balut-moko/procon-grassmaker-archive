N, M = map(int, input().split())
A = list(map(int, input().split()))


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        tmp = 0
        for a in A:
            tmp += min(mid, a)
        return tmp <= M

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = meguru_bisect(0, 1 << 60)

print(ans if ans < 1 << 30 else "infinite")
