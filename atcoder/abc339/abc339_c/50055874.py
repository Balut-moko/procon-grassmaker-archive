N = int(input())
A = list(map(int, input().split()))


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        for a in A:
            mid += a
            if mid < 0:
                return False
        return True

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


cnt = meguru_bisect(1 << 60, -1)
for a in A:
    cnt += a

print(cnt)
