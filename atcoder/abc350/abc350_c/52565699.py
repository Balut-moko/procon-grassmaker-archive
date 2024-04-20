N = int(input())
A = list(map(int, input().split()))

idx_di = {v: i for i, v in enumerate(A)}
ans = []
for i in range(N - 1):
    if A[i] == i + 1:
        continue
    idx = idx_di[i + 1]
    A[i], A[idx] = A[idx], A[i]
    idx_di[A[idx]] = idx
    ans.append((i + 1, idx + 1))

print(len(ans))
for v in ans:
    print(*v)
