from collections import deque


N = int(input())
TX = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in [0] * N]

cnt = [0] * N
act = deque([])
used = [0] * N
for t, x in TX:
    if t == 0:
        cnt[x] += 1


for i in range(N - 1, -1, -1):
    t, x = TX[i]
    if t == 0:
        if used[x] > 0:
            used[x] -= 1
            act.appendleft(1)
        else:
            act.appendleft(0)
    else:
        if cnt[x] > 0:
            cnt[x] -= 1
            used[x] += 1
        else:
            print(-1)
            exit()


ans_act = list(act)
K = 0
tmp = 0
for i in range(N):
    t, x = TX[i]
    if t == 0:
        a = act.popleft()
        if a == 1:
            tmp += 1
            K = max(K, tmp)
    else:
        tmp -= 1

print(K)
print(*ans_act)
