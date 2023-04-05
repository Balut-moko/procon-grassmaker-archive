from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

S = [0]
C = [0]

for _ in range(m):
    s, c = readline().split()
    s_val = 0
    for i in range(n):
        if s[i] == "Y":
            s_val |= 1 << i
    S.append(s_val)
    C.append(int(c))

ALL = 1 << n
dp = [[1 << 60] * ALL for _ in [0] * (m + 1)]

dp[0][0] = 0

for i in range(1, m + 1):
    for j in range(ALL):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        dp[i][j | S[i]] = min(dp[i][j | S[i]], dp[i - 1][j] + C[i])

ans = dp[m][ALL - 1]

print(ans if ans != 1 << 60 else -1)
