N = int(input())

dp = list(map(int, input().split()))

for i in range(1, N):
    a, b, c = map(int, input().split())
    ndp = [0] * 3
    ndp[0] = max(dp[1], dp[2]) + a
    ndp[1] = max(dp[2], dp[0]) + b
    ndp[2] = max(dp[0], dp[1]) + c
    dp = ndp

print(max(dp))
