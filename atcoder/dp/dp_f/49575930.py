S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in [0] * (len(S) + 1)]

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])

ans = ""
i = len(S)
j = len(T)
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans = S[i - 1] + ans
        i -= 1
        j -= 1

print(ans)
