from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

cnt1, cnt2, cnt3 = a.count(1), a.count(2), a.count(3)
dp = [[[0.0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

for k in range(cnt3 + 1):
    for j in range(cnt2 + cnt3 + 1 - k):
        for i in range(cnt1 + cnt2 + cnt3 + 1 - k - j):
            if i == j == k == 0:
                continue
            tmp = n

            if i > 0:
                tmp += i * dp[i - 1][j][k]
            if j > 0:
                tmp += j * dp[i + 1][j - 1][k]
            if k > 0:
                tmp += k * dp[i][j + 1][k - 1]
            dp[i][j][k] = tmp / (i + j + k)

print(dp[cnt1][cnt2][cnt3])
