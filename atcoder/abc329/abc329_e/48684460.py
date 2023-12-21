from collections import deque


N, M = map(int, input().split())
S = list(input())
T = list(input())

used = [False] * (N - M + 1)
que = deque([])


def check(i):
    if used[i]:
        return
    ok = True
    for j in range(M):
        ok &= S[i + j] == "#" or S[i + j] == T[j]
    if ok:
        used[i] = True
        que.append(i)


for i in range(N - M + 1):
    check(i)

while que:
    i = que.popleft()
    for j in range(M):
        S[i + j] = "#"
    for j in range(max(0, i - M + 1), min(N - M + 1, i + M)):
        check(j)

print("Yes" if S == ["#"] * N else "No")
