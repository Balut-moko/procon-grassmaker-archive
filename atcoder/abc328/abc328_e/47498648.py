import sys

sys.setrecursionlimit(10**7)
N, M, K = map(int, input().split())
UVC = [tuple(map(int, input().split())) for _ in range(M)]

ans = [1 << 60]


def has_bit(n, i):
    return n & (1 << i) > 0


def dfs(S, cost):
    if S == (1 << N) - 1:
        ans[0] = min(ans[0], cost % K)
        return
    for i in range(M):
        u, v, c = UVC[i]
        u -= 1
        v -= 1
        if has_bit(S, u) and has_bit(S, v):
            continue
        if not has_bit(S, u) and not has_bit(S, v):
            continue
        if has_bit(S, u) and not has_bit(S, v):
            S |= 1 << v
            cost += c
            dfs(S, cost)
            S -= 1 << v
            cost -= c
            continue
        if not has_bit(S, u) and has_bit(S, v):
            S |= 1 << u
            cost += c
            dfs(S, cost)
            S -= 1 << u
            cost -= c
            continue


S = 1
dfs(S, 0)
print(ans[0])
