from bisect import bisect_left


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0

for i in range(N):
    x = A[i]
    idx = bisect_left(A, x + M)
    ans = max(ans, idx - i)

print(ans)
