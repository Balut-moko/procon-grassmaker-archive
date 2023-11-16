N = int(input())
P = [int(input()) for _ in [0] * N]

dic = dict()

for i in range(N):
    dic[P[i] - 1] = i
ans = 0
i = 0
while i < N:
    now = dic[i]
    cnt = 0
    while i < N and now <= dic[i]:
        now = dic[i]
        cnt += 1
        i += 1
    if i != N:
        i -= 1
    ans = max(ans, cnt)
    i += 1
print(N - ans)
