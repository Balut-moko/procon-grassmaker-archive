from bisect import bisect_right
from itertools import accumulate


N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
AA = sorted(A)
cs = list(accumulate(AA, initial=0))
ans = [0] * N
for i in range(N):
    idx = bisect_right(AA, A[i])
    ans[i] = sum_A - cs[idx]

print(*ans)
