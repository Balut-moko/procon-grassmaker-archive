N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
ans = N
tmp = 0
for i in range(N):
    tmp += A[i]
    if X < tmp:
        ans = min(ans, i + 1)
tmp = 0
for i in range(N):
    tmp += B[i]
    if Y < tmp:
        ans = min(ans, i + 1)

print(ans)
