N = int(input())
A = [tuple(map(int, input().split())) for _ in [0] * N]

score = [0] * (1 << N)
for s in range(1 << N):
    for i in range(N):
        for j in range(i + 1, N):
            if s & (1 << i) == 0 or s & (1 << j) == 0:
                continue
            score[s] += A[i][j]

dp = [0] * (1 << N)
for s in range(1 << N):
    t = s
    while t >= 0:
        t &= s
        dp[s] = max(dp[s], dp[t] + score[s - t])
        t -= 1

print(dp[-1])
