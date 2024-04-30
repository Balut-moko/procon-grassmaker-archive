from atcoder.fenwicktree import FenwickTree
import bisect

N = int(input())
A = list(map(int, input().split()))
B = sorted([x for x in set(A)])
M = len(B)
sum0 = FenwickTree(M)
sum1 = FenwickTree(M)
ans = 0
for i in reversed(range(N)):
    k = bisect.bisect_left(B, A[i])
    c = sum0.sum(k, M)
    s = sum1.sum(k, M)
    ans += s - c * A[i]
    sum0.add(k, 1)
    sum1.add(k, A[i])
print(ans)
