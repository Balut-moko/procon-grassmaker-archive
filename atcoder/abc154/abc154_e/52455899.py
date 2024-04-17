from itertools import product


N = input()
K = int(input())

n = len(N)
dp = [[[0] * (K + 2) for _ in [0] * 2] for _ in [0] * (n + 1)]
dp[0][0][0] = 1

for i, smaller, j in product(range(n), (0, 1), range(K + 1)):
    max_d = 9 if smaller else int(N[i])
    for x in range(max_d + 1):
        nx = j if x == 0 else j + 1  # 遷移先
        dp[i + 1][smaller or x < max_d][nx] += dp[i][smaller][j]

print(dp[-1][0][K] + dp[-1][1][K])
