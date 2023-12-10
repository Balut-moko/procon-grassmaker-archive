from collections import deque
import sys

sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
A = tuple([tuple(map(int, input().split())) for _ in [0] * H])
B = tuple([tuple(map(int, input().split())) for _ in [0] * H])

p = set()
ans = 1 << 60
que = deque([[A, 0]])


def check(A):
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[i][j]:
                return False
    return True


while que:
    a, cnt = que.popleft()
    if check(a):
        ans = min(ans, cnt)
        continue

    for i in range(H - 1):
        AA = [v for v in a]
        AA[i], AA[i + 1] = AA[i + 1], AA[i]
        AA = tuple(AA)
        if AA not in p:
            p.add(AA)
            que.append([AA, cnt + 1])
    for j in range(W - 1):
        AA = list(zip(*a))
        AA[j], AA[j + 1] = AA[j + 1], AA[j]
        AA = tuple(zip(*AA))
        if AA not in p:
            p.add(AA)
            que.append([AA, cnt + 1])


print(ans if ans != 1 << 60 else -1)
