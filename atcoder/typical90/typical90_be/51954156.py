N, M = map(int, input().split())

dp = [[0] * M for _ in range(N)]

for i in range(N):
    T = int(input())
    X = list(map(int, input().split()))
    for x in X:
        x -= 1
        dp[i][x] = 1

S = list(map(int, input().split()))

pos = 0
for i in range(M):
    found = False
    for j in range(pos, N):
        if dp[j][i] == 1:
            found = True
            if j != pos:
                dp[j], dp[pos] = dp[pos], dp[j]
            break
    if found:
        for j in range(N):
            if j != pos and dp[j][i] == 1:
                for k in range(i, M):
                    dp[j][k] ^= dp[pos][k]
        if S[i] == 1:
            for j in range(i, M):
                S[j] ^= dp[pos][j]
        pos += 1

if S == [0] * M:
    print(pow(2, N - pos, 998244353))
else:
    print(0)
