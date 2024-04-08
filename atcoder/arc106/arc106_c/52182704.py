N, M = map(int, input().split())
if M == 0:
    for i in range(N):
        print(2 * i + 1, 2 * i + 2)
    exit()
if not (0 <= M <= N - 2):
    print(-1)
    exit()
ans = []
for i in range(N):
    ans.append((3 * i + 1, 3 * i + 2))
ans[0] = [1, ans[M + 1][1] + 1]
for lr in ans:
    print(*lr)
