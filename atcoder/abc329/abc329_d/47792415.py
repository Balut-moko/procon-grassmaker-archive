N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * (N + 1)
ans = [0] * M
cnt[A[0]] += 1
ans[0] = A[0]
pre = A[0]

for i in range(1, M):
    p = A[i]
    cnt[p] += 1
    if cnt[pre] < cnt[p]:
        ans[i] = p
        pre = p
    elif cnt[pre] == cnt[p]:
        ans[i] = min(pre, p)
        pre = min(pre, p)
    else:
        ans[i] = pre

print(*ans, sep="\n")
