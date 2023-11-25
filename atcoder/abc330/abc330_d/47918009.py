N = int(input())
S = [input() for _ in [0] * N]
ans = 0
r_cnt = [0] * N
c_cnt = [0] * N
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            r_cnt[i] += 1
            c_cnt[j] += 1

for i in range(N):
    for j in range(N):
        if S[i][j] == "x":
            continue
        ans += (r_cnt[i] - 1) * (c_cnt[j] - 1)

print(ans)
