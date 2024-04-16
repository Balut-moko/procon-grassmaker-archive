N = int(input())
A = [int(input()) for _ in [0] * N]
if A[0] != 0:
    print(-1)
    exit()

for i in range(1, N):
    if A[i] - A[i - 1] > 1:
        print(-1)
        exit()

ans = 0
for i in range(1, N):
    if A[i] - A[i - 1] != 1:
        ans += A[i - 1]
ans += A[-1]
print(ans)
