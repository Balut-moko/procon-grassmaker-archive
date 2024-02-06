from collections import defaultdict


N = int(input())
A = [int(input()) for _ in [0] * N]
A.sort()

di = defaultdict(int)

for a in A:
    di[a] += 1

ans = 0
for i in range(N):
    for j in range(N):
        aij = A[i] * A[j]
        if A[-1] < aij:
            break
        ans += di[aij]

print(ans)
