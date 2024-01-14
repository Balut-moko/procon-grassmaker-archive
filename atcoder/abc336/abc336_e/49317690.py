from itertools import product

N = input()
n = len(N)
D = 140
ans = 0
for D in range(1, 127):
    dp = [[[[0] * D for _ in [0] * (D + 1)] for _ in [0] * 2] for _ in [0] * (n + 1)]
    dp[0][0][0][0] = 1

    for i, smaller, j, k in product(range(n), (0, 1), range(D), range(D + 1)):
        max_d = 9 if smaller else int(N[i])
        for x in range(max_d + 1):
            if k + x > D:
                break
            nx = (10 * j + x) % D  # 遷移先
            dp[i + 1][smaller or x < max_d][k + x][nx] += dp[i][smaller][k][j]
    ans += dp[n][0][D][0] + dp[n][1][D][0]

print(ans)
