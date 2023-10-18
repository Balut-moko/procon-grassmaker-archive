N, T = input().split()
N = int(N)
M = len(T)
S = [input() for _ in [0] * N]

left = [0] * (M + 1)
right = [0] * (M + 2)
right[-1] = N
idx_li = [0] * N

for i in range(N):
    idx = 0
    for v in S[i]:
        if M <= idx:
            break
        if T[idx] == v:
            idx += 1
            left[idx] += 1
    idx_li[i] = idx
    idx = -1
    for j in range(len(S[i]) - 1, -1, -1):
        if idx < -M:
            break
        if T[idx] == S[i][j]:
            idx -= 1
            right[idx] += 1
ans = 0
for i in idx_li:
    ans += right[i + 1]

print(ans)
