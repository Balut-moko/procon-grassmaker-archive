from sys import stdin

readline = stdin.readline
n = int(readline())

xyz = [tuple(map(int, readline().split())) for _ in [0] * n]
z_sum = sum([z for x, y, z in xyz])


dp = [[1 << 60] * (10 ** 5 + 1) for _ in [0] * n]

if xyz[0][0] < xyz[0][1]:
    dp[0][0] = 0
    dp[0][xyz[0][2]] = (xyz[0][1] - xyz[0][0] + 1) // 2
else:
    dp[0][xyz[0][2]] = 0

for i in range(1, n):
    x, y, z = xyz[i]
    for j in range(10 ** 5 + 1):
        if x < y:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            if j - z >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - z] + (y - x + 1) // 2)
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - z])
ans = 1 << 60
for j in range((z_sum + 1) // 2, 10 ** 5 + 1):
    ans = min(ans, dp[-1][j])

print(ans)
