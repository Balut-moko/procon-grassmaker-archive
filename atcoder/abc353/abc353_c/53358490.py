from bisect import bisect_left
from itertools import accumulate


N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
AS_sum = list(accumulate(A, initial=0))

ans = 0
for i in range(N - 1):
    idx = bisect_left(A, 10**8 - A[i])
    ans += AS_sum[N] - AS_sum[i + 1]
    ans += A[i] * (N - i - 1)
    ans -= min(N - i - 1, N - idx) * 10**8

print(ans)
