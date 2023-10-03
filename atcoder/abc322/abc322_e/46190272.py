N, K, P = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in [0] * N]

INF = 1 << 60
dp = dict()

dp[tuple([0 for _ in range(K)])] = 0

for i in range(N):
    c, *a = A[i]
    items = list(dp.items())
    for key, val in items:
        nkey = tuple([min(P, key[k] + a[k]) for k in range(K)])
        cost = dp.get(nkey, INF)
        dp[nkey] = min(cost, val + c)
ans = dp.get(tuple([P for _ in range(K)]), -1)
print(ans)
