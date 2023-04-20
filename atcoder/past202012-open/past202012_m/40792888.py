from itertools import accumulate
from sys import stdin

readline = stdin.readline
n, L = map(int, readline().split())
a = list(map(int, readline().split()))
s = [0] + list(accumulate(a))


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        l = 0
        r = 0
        flag = [0] * (n + 1)
        d = [0] * (n + 1)
        d[0] = 1
        d[1] = -1
        flag[0] = 1
        for i in range(n):
            if i > 0:
                flag[i] = flag[i - 1] + d[i]
            if flag[i] == 0:
                continue
            while l <= n and s[l] - s[i] < mid:
                l += 1
            if l > n:
                continue

            while r + 1 <= n and s[r + 1] - s[i] <= L:
                r += 1
            d[l] += 1
            if r + 1 <= n:
                d[r + 1] -= 1
        flag[n] = flag[n - 1] + d[n]
        return flag[n] > 0

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, L + 1))
