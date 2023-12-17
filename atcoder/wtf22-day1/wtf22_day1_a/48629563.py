N, M, A, B = map(int, input().split())
X = list(map(int, input().split()))
cnt = [0] * N

for x in X:
    cnt[x - 1] += 1
cnt.sort()
ans = max(0, N + B - A)
s = 0
for i in range(N):
    s += cnt[i]
    if s <= B:
        ans = max(ans, i + 1)
print(ans)
