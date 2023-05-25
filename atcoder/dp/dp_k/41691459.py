from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))

dp = [0] * 100001

for j in range(k + 1):
    lose = 0
    cnt = 0
    for i in range(n):
        if 0 <= j - a[i]:
            cnt += 1
            if not dp[j - a[i]]:
                lose += 1
        if cnt == 0:
            dp[j] = 0
        elif 0 < lose:
            dp[j] = 1
        else:
            dp[j] = 0

print("First" if dp[k] else "Second")
