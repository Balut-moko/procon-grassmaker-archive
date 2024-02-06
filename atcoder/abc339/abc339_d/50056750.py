from collections import deque


N = int(input())
S = [list(input()) for _ in [0] * N]
A = (-1, -1)
B = (-1, -1)


def idx(P):
    r, c = P
    return r * N + c


for r in range(N):
    for c in range(N):
        if S[r][c] == "P":
            if A == (-1, -1):
                A = (r, c)
            else:
                B = (r, c)

dp = [[1 << 60] * N * N for _ in [0] * N * N]

que = deque([(A, B)])
dp[idx(A)][idx(B)] = 0
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
while que:
    a, b = que.popleft()
    cur = dp[idx(a)][idx(b)]
    for dr, dc in dd:
        ar = a[0] + dr
        ac = a[1] + dc
        na = (ar, ac)
        if not (0 <= ar < N and 0 <= ac < N) or S[ar][ac] == "#":
            na = a
        br = b[0] + dr
        bc = b[1] + dc
        nb = (br, bc)
        if not (0 <= br < N and 0 <= bc < N) or S[br][bc] == "#":
            nb = b
        if idx(na) > idx(nb):
            na, nb = nb, na
        if cur + 1 < dp[idx(na)][idx(nb)]:
            dp[idx(na)][idx(nb)] = cur + 1
            que.append((na, nb))
ans = 1 << 60
for i in range(N * N):
    ans = min(ans, dp[i][i])

print(ans if ans != 1 << 60 else -1)
