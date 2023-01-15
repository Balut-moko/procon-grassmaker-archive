from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

if n == 1:
    print(0)
    exit()


score_li = [0] * (n * 2 + 1)
for x in range(1, n):
    for y in range(1, n):
        score_li[x + y] += a[min(x - 1, y - 1)]

dp = [0] * (n + 1)

for i in range(n + 1):
    for k in range(i + 1):
        dp[i] = max(dp[i], dp[i - k] + score_li[k])

print(max(dp))
