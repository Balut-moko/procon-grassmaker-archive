from itertools import product


def count(N):
    N = str(N)
    n = len(N)
    dp = [[[[0] * 10 for _ in [0] * 2] for _ in [0] * (n + 1)] for _ in [0] * 2]

    dp[1][0][0][0] = 1

    for i, lz, smaller, j in product(range(n), (0, 1), (0, 1), range(10)):
        max_d = 9 if smaller else int(N[i])
        for x in range(max_d + 1):
            lz2 = lz
            if x != 0:
                lz2 = 0
            if x != j:
                dp[lz2][i + 1][smaller or x < max_d][x] += dp[lz][i][smaller][j]
            elif lz2 == 1:
                dp[lz2][i + 1][smaller or x < max_d][x] += dp[lz][i][smaller][j]
    return sum(dp[0][-1][1]) + sum(dp[0][-1][0])


def solve(mid: int):
    cnt = count(mid)
    return cnt < K


def meguru_bisect(ok: int, ng: int):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


T = int(input())
for _ in range(T):
    K = int(input())
    ans = meguru_bisect(0, 1 << 60)
    print(ans + 1)
