N, M = map(int, input().split())
S = [input() for _ in [0] * N]

dp = [1 << 60] * N
dpr = [1 << 60] * N

dp[0] = 0

for i in range(1, N):
    for j in range(1, min(M, i) + 1):
        if S[i - j][j - 1] == "1":
            dp[i] = min(dp[i], dp[i - j] + 1)

dpr[N - 1] = 0

for i in range(N - 2, -1, -1):
    for j in range(1, min(M + 1, N - i)):
        if S[i][j - 1] == "1":
            dpr[i] = min(dpr[i], dpr[i + j] + 1)

ans = [-1] * (N - 2)

for k in range(1, N - 1):
    tmp = 1 << 60
    for i in range(max(k - M + 1, 0), k):
        for j in range(k + 1, min(N, i + M + 1)):
            if S[i][j - i - 1] == "1":
                tmp = min(tmp, dp[i] + dpr[j] + 1)
    if tmp != 1 << 60:
        ans[k - 1] = tmp
print(*ans)
