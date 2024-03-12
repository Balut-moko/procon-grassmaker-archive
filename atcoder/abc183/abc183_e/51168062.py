H, W = map(int, input().split())
S = [input() for _ in [0] * H]
MOD = 10**9 + 7
dp = [[0] * W for _ in [0] * H]
dp[0][0] = 1
rdp = [[0] * W for _ in [0] * H]
rdp[0][0] = 1
cdp = [[0] * W for _ in [0] * H]
cdp[0][0] = 1
rcdp = [[0] * W for _ in [0] * H]
rcdp[0][0] = 1

for r in range(H):
    for c in range(W):
        if r == c == 0:
            continue
        if r != 0:
            dp[r][c] += rdp[r - 1][c]
        if c != 0:
            dp[r][c] += cdp[r][c - 1]
        if r != 0 and c != 0:
            dp[r][c] += rcdp[r - 1][c - 1]
        if S[r][c] == "#":
            dp[r][c] = 0
            continue
        dp[r][c] %= MOD
        rdp[r][c] = dp[r][c]
        cdp[r][c] = dp[r][c]
        rcdp[r][c] = dp[r][c]

        if r != 0:
            rdp[r][c] += rdp[r - 1][c]
            rdp[r][c] %= MOD
        if c != 0:
            cdp[r][c] += cdp[r][c - 1]
            cdp[r][c] %= MOD
        if r != 0 and c != 0:
            rcdp[r][c] += rcdp[r - 1][c - 1]
            rcdp[r][c] %= MOD

print(dp[-1][-1])
