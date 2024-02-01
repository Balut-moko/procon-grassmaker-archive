N, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in [0] * N]
MOD = 10**9 + 7


def mul(a, b):
    res = [[0] * N for _ in [0] * N]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += a[i][k] * b[k][j]
                res[i][j] %= MOD
    return res


def pow_matrix(m, k):
    res = [[0] * N for _ in [0] * N]
    for i in range(N):
        res[i][i] = 1

    while k > 0:
        if k & 1:
            res = mul(res, m)
        m = mul(m, m)
        k >>= 1
    return res


A = pow_matrix(A, K)

ans = 0
for i in range(N):
    for j in range(N):
        ans += A[i][j]
        ans %= MOD

print(ans)
