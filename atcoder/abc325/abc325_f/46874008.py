N = int(input())
D = list(map(int, input().split()))
L1, C1, K1 = map(int, input().split())
L2, C2, K2 = map(int, input().split())

dp = [[1 << 60] * (K1 + 1) for _ in [0] * (N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(K1 + 1):
        rem = D[i]
        for nj in range(j, K1 + 1):
            dp[i + 1][nj] = min(dp[i + 1][nj], dp[i][j] + (rem + L2 - 1) // L2)
            rem = max(rem - L1, 0)

ans = 1 << 60
for i in range(K1 + 1):
    if dp[N][i] > K2:
        continue
    ans = min(ans, C1 * i + C2 * dp[N][i])
if ans >= 1 << 59:
    ans = -1
print(ans)
