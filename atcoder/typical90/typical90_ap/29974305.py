from sys import stdin

readline = stdin.readline
k = int(readline())

if k % 9 != 0:
    print(0)
    exit()

mod = 10 ** 9 + 7
dp = [0] * (k + 1)
dp[0] = 1

for i in range(1, k + 1):
    b = min(i, 9)
    for j in range(1, b + 1):
        dp[i] += dp[i - j]
        dp[i] %= mod
print(dp[k])
