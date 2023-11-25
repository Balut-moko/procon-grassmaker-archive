N, L = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    if L <= A[i]:
        ans += 1
print(ans)
