from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))

dp = [[False] * (sum(p) + 1) for _ in [0] * n]
for i, val in enumerate(p):
    if i == 0:
        dp[i][0] = True
        dp[i][val] = True
        continue
    for s in range(sum(p) + 1):
        if dp[i - 1][s]:
            dp[i][s] = True
        if s - val >= 0 and dp[i - 1][s - val]:
            dp[i][s] = True
print(sum(dp[-1]))
