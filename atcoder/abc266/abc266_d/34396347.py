from sys import stdin

readline = stdin.readline
n = int(readline())

txa = [tuple(map(int, readline().split())) for _ in [0] * n]
txa_di = {t: (x, a) for t, x, a in txa}
dp = [[0] * 5 for _ in [0] * (10 ** 5 + 1)]

for i in range(1, 10 ** 5 + 1):
    x, a = txa_di.get(i, (0, 0))
    if i == 1:
        if x <= 1:
            dp[1][x] = a
    elif i == 2:
        dp[2][0] = max(dp[1][0], dp[1][1])
        dp[2][1] = max(dp[1][0], dp[1][1])
        dp[2][2] = dp[1][1]
        if x <= 2:
            dp[2][x] += a
    elif i == 3:
        dp[3][0] = max(dp[2][0], dp[2][1])
        dp[3][1] = max((dp[2][0], dp[2][1], dp[2][2]))
        dp[3][2] = max(dp[2][1], dp[2][2])
        dp[3][3] = dp[2][2]
        if x <= 3:
            dp[3][x] += a
    elif i == 4:
        dp[4][0] = max(dp[3][0], dp[3][1])
        dp[4][1] = max((dp[3][0], dp[3][1], dp[3][2]))
        dp[4][2] = max((dp[3][1], dp[3][2], dp[3][3]))
        dp[4][3] = max(dp[3][2], dp[3][3])
        dp[4][4] = dp[3][3]
        dp[4][x] += a
    else:
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = max((dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]))
        dp[i][2] = max((dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]))
        dp[i][3] = max((dp[i - 1][2], dp[i - 1][3], dp[i - 1][4]))
        dp[i][4] = max(dp[i - 1][3], dp[i - 1][4])
        dp[i][x] += a

print(max(dp[-1]))
