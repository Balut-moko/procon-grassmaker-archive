from collections import defaultdict
from itertools import accumulate


N, M = map(int, input().split())
A = list(map(int, input().split()))
A = A + A

cs = list(accumulate(A, initial=0))
cs = [v % M for v in cs]
di = defaultdict(int)

for i in range(1, N):
    di[cs[i]] += 1

ans = di[cs[0]]
di[cs[N]] += 1

for i in range(1, N):
    ans += di[cs[i]] - 1
    di[cs[i]] -= 1
    di[cs[i + N]] += 1


print(ans)
