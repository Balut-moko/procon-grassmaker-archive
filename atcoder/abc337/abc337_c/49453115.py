N = int(input())
A = list(map(int, input().split()))

d = {v: i + 1 for i, v in enumerate(A)}
ans = [0] * N
ans[0] = d[-1]

for i in range(1, N):
    ans[i] = d[ans[i - 1]]

print(*ans)
