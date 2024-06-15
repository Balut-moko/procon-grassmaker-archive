N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
ans = 0
cur = 0
for a in A:
    if B[cur] <= a:
        ans += a
        cur += 1
    if cur == M:
        print(ans)
        exit()
print(-1)
