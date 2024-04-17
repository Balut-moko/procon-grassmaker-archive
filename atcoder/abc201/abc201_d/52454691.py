H, W = map(int, input().split())
A = [input() for _ in [0] * H]

dp = [[-1 << 60] * W for _ in [0] * H]

dp[-1][-1] = 0

for r in range(H - 1, -1, -1):
    for c in range(W - 1, -1, -1):
        if r + 1 < H:
            p = 1 if A[r + 1][c] == "+" else -1
            dp[r][c] = max(dp[r][c], -dp[r + 1][c] + p)
        if c + 1 < W:
            p = 1 if A[r][c + 1] == "+" else -1
            dp[r][c] = max(dp[r][c], -dp[r][c + 1] + p)

if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] < 0:
    print("Aoki")
else:
    print("Draw")
