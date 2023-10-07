N = int(input())
S = [input() for _ in [0] * N]
cnt = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        if S[i][j] == "o":
            cnt[i] -= 1
        else:
            cnt[j] -= 1

cnt = [(v, i) for i, v in enumerate(cnt)]

cnt.sort()

ans = []
for v, i in cnt:
    ans.append(i + 1)

print(*ans)
