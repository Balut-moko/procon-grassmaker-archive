from bisect import bisect_left


N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = [0] * N

for i in range(1, N + 1):
    idx = bisect_left(A, i)
    ans[i - 1] = A[idx] - i

print(*ans, sep="\n")
