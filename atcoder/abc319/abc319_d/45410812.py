from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
L = list(map(int, readline().split()))


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        cnt = 0
        tmp = 0
        for i in range(n):
            tmp += L[i]
            if mid < tmp:
                cnt += 1
                tmp = L[i]
                if mid == tmp:
                    cnt += 1
                    tmp = 0
                else:
                    tmp += 1
            elif mid == tmp:
                cnt += 1
                tmp = 0
            else:
                tmp += 1
        if tmp > 0:
            cnt += 1
        return cnt <= m

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(1 << 60, max(L) - 1))
