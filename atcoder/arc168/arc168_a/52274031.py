N = int(input())
S = input()
cnt = [0] * N
tmp = 0
for i in range(N - 2, -1, -1):
    if S[i] == ">":
        tmp += 1
    else:
        tmp = 0
    cnt[i] = tmp

ans = 0
for i, s in enumerate(S):
    if s == ">":
        ans += cnt[i]

print(ans)
