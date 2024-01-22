H, W = map(int, input().split())
S = [input() for _ in [0] * H]

dp = [[0] * W for _ in [0] * H]
dp[0][0] = 1
MOD = 10**9 + 7
for r in range(H):
    for c in range(W):
        if S[r][c] == "#":
            continue
        if r + 1 < H and S[r + 1][c] == ".":
            dp[r + 1][c] += dp[r][c]
            dp[r + 1][c] %= MOD
        if c + 1 < W and S[r][c + 1] == ".":
            dp[r][c + 1] += dp[r][c]
            dp[r][c + 1] %= MOD

print(dp[-1][-1])
