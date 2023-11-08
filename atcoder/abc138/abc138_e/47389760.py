S = input()
T = input()
SS = S + S


def calc_next(S):
    N = len(S)
    nex = [[N] * 26 for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(26):
            nex[i][j] = nex[i + 1][j]
        nex[i][ord(S[i]) - ord("a")] = i
    return nex


if set(list(T)) - set(list(S)):
    print(-1)
    exit()

nex = calc_next(SS)
pre, now = 0, 0
ans = 0
for t in T:
    pre = ans % len(S)
    now = nex[pre][ord(t) - ord("a")]
    ans += now - pre + 1

print(ans)
