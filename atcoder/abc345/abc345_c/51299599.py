S = input()
N = len(S)
dp = [[0] * 26 for _ in [0] * (N + 1)]
for i in range(N):
    dp[i + 1][ord(S[i]) - ord("a")] += 1

for i in range(N - 1, -1, -1):
    for j in range(26):
        dp[i][j] += dp[i + 1][j]

ans = 0
for i in range(N):
    for j in range(26):
        if S[i] == chr(ord("a") + j):
            continue
        ans += dp[i + 1][j]

flag = False
for j in range(26):
    if dp[0][j] > 1:
        flag = True

if flag:
    ans += 1
print(ans)
