from itertools import accumulate


N, K = map(int, input().split())
A = list(map(int, input().split()))

if K % 2 == 0:
    ans = 0
    for i in range(0, K, 2):
        ans += A[i + 1] - A[i]
    print(ans)
    exit()

L = [A[i + 1] - A[i] for i in range(0, K - 1, 2)]
Lcum = list(accumulate(L, initial=0))
R = [A[i] - A[i - 1] for i in range(K - 1, 0, -2)]
Rcum = list(accumulate(R, initial=0))
Rcum = Rcum[::-1]
ans = 1 << 60
for i in range(0, K, 2):
    ans = min(ans, Lcum[i // 2] + Rcum[i // 2])

print(ans)
