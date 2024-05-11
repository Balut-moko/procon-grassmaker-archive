N, K = map(int, input().split())
A = list(map(int, input().split()))

now = 0
cnt = 0
idx = 0
while idx < N:
    if now + A[idx] <= K:
        now += A[idx]
        idx += 1
    else:
        cnt += 1
        now = 0

if now != 0:
    cnt += 1

print(cnt)
