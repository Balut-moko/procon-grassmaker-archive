N = int(input())
A = list(map(int, input().split()))


if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()

cnt = []
for i in range(N + 1):
    if i == 0:
        if A[0] == 0:
            cnt.append(1)
            continue
        print(-1)
        exit()
    x = cnt[-1] * 2
    if x - A[i] >= 0:
        cnt.append(x - A[i])
        continue
    print(-1)
    exit()

cnt[N] = 0

ans = [0] * (N + 1)
ans[N] = A[N]
for i in range(N - 1, -1, -1):
    ans[i] = min(cnt[i], ans[i + 1]) + A[i]

print(sum(ans))
