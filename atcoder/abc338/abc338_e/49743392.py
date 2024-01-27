from collections import deque

N = int(input())
AB = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in [0] * N]

v = [None] * (2 * N)
for i in range(N):
    a, b = AB[i]
    if a > b:
        a, b = b, a
    v[a] = (0, i)
    v[b] = (1, i)

que = deque([])
flag = False
for i in range(2 * N):
    t, idx = v[i]
    if t == 0:
        que.append(idx)
    else:
        top = que.pop()
        if top != idx:
            flag = True
            break

print("Yes" if flag else "No")
