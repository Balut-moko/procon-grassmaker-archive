N = int(input())
A = list(map(int, input().split()))

cl = [0] * N
cr = [0] * N
cnt = 0
for i in range(N):
    if cnt < A[i]:
        cnt += 1
    else:
        cnt = A[i]
    cl[i] = cnt
cnt = 0
for i in range(N - 1, -1, -1):
    if cnt < A[i]:
        cnt += 1
    else:
        cnt = A[i]
    cr[i] = cnt

ans = 0
for i in range(N):
    ans = max(ans, min(cl[i], cr[i]))

print(ans)
