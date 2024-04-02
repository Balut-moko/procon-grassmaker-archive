def has_bit(n, i):
    return n & (1 << i) > 0


def calc_dist(p, q):
    return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])


N, K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in [0] * N]
ALL = 1 << N
dist = [[0] * N for _ in [0] * N]

for i in range(N):
    for j in range(i):
        d = calc_dist(XY[i], XY[j])
        dist[i][j] = dist[j][i] = d

mx_d = [0] * ALL

for bit in range(ALL):
    if bit.bit_count() <= 1:
        continue
    i = bit.bit_length() - 1
    d = mx_d[bit ^ 1 << i]
    for j in range(N):
        if has_bit(bit, j):
            d = max(d, dist[i][j])
    mx_d[bit] = d

INF = 1 << 60
dp = [[INF] * ALL for _ in [0] * (K + 1)]
dp[0][0] = 0

mask = ALL - 1

for i in range(K):
    for j in range(ALL):
        pre = dp[i][j]
        a = b = mask ^ j
        while a > 0:
            t = max(pre, mx_d[a])
            dp[i + 1][j | a] = min(dp[i + 1][j | a], t)
            a = (a - 1) & b

print(dp[-1][-1])
