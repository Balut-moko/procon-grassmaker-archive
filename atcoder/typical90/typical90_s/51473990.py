N = int(input())
A = list(map(int, input().split()))
N *= 2
INF = 10**9 + 7
dp = [[INF] * (N + 1) for _ in [0] * (N + 1)]

for d in range(N // 2 + 1):
    for l in range(N):
        r = l + 2 * d
        if d == 0:
            dp[l][r] = 0
            continue
        if N < r:
            break
        for k in range(d):
            m = l + 2 * k + 1
            dp[l][r] = min(dp[l][r], dp[l + 1][m] + abs(A[m] - A[l]) + dp[m + 1][r])
        dp[l][r] = min(dp[l + 1][r - 1] + abs(A[l] - A[r - 1]), dp[l][r])

print(dp[0][N])
