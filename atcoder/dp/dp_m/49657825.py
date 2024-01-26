N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (K + 1) for _ in [0] * (N + 1)]
dp[0][0] = 1
MOD = 10**9 + 7

for i in range(N):
    sdp = [0] * (K + 2)
    for j in range(K + 1):
        sdp[j + 1] = sdp[j] + dp[i][j]
        sdp[j + 1] %= MOD
    for j in range(K + 1):
        dp[i + 1][j] = sdp[j + 1] - sdp[j - min(j, A[i])]
        dp[i + 1][j] %= MOD
print(dp[N][K])
