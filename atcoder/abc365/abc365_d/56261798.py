N = int(input())
S = input()

dp = [[0] * 3 for _ in [0] * N]
aoki = S[0]
# "R" -> 0
# "P" -> 1
# "S" -> 2

if aoki == "R":
    dp[0][1] = 1
elif aoki == "P":
    dp[0][2] = 1
else:
    dp[0][0] = 1

for i in range(1, N):
    aoki = S[i]
    if aoki == "R":
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + 1

    elif aoki == "P":
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + 1
    else:
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + 1

print(max(dp[-1]))
