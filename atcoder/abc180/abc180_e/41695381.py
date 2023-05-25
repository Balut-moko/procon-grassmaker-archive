from sys import stdin

readline = stdin.readline
N = int(readline())
p = [tuple(map(int, readline().split())) for _ in [0] * N]


def calc_cost(pre, to):
    return abs(to[0] - pre[0]) + abs(to[1] - pre[1]) + max(0, to[2] - pre[2])


def has_bit(n, i):
    return n & (1 << i) > 0


ALL = 1 << N
dp = [[1 << 60] * N for _ in [0] * ALL]

dp[1][0] = 0

for n in range(ALL):
    for i in range(N):
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            dp[n | (1 << j)][j] = min(
                dp[n | (1 << j)][j], dp[n][i] + calc_cost(p[i], p[j])
            )

ans = 1 << 60
for i in range(N):
    ans = min(ans, dp[-1][i] + calc_cost(p[i], p[0]))

print(ans)
