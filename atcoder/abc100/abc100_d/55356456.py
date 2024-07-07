def has_bit(n, i):
    return n & (1 << i) > 0


N, M = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in [0] * N]
ans = -1 << 60
for n in range(1 << 3):
    p = []
    dp = [[-1 << 60] * (M + 2) for _ in [0] * (N + 1)]
    dp[0][0] = 0
    for i in range(N):
        x, y, z = xyz[i]
        if has_bit(n, 0):
            x *= -1
        if has_bit(n, 1):
            y *= -1
        if has_bit(n, 2):
            z *= -1
        p = x + y + z
        for j in range(M + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + p)
    ans = max(ans, dp[N][M])

print(ans)
