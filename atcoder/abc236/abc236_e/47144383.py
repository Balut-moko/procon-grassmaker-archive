N = int(input())
A = list(map(int, input().split()))


def check_avg(x):
    B = [a - x for a in A]
    dp = [[0] * 2 for _ in [0] * (N + 1)]

    for i in range(N):
        dp[i + 1][1] = max(dp[i][0], dp[i][1]) + B[i]
        dp[i + 1][0] = dp[i][1]
    return max(dp[N][0], dp[N][1]) > 0


def meguru_bisect_f(ok: float, ng: float):
    for _ in range(100):
        mid = (ok + ng) / 2
        if check_avg(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect_f(0, 10**10))


def check_median(x):
    B = [1 if a >= x else -1 for a in A]
    dp = [[0] * 2 for _ in [0] * (N + 1)]

    for i in range(N):
        dp[i + 1][1] = max(dp[i][0], dp[i][1]) + B[i]
        dp[i + 1][0] = dp[i][1]
    return max(dp[N][0], dp[N][1]) > 0


def meguru_bisect(ok: int, ng: int):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check_median(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, 10**10))
