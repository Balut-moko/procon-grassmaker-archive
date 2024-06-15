N, M = map(int, input().split())
S = [input() for _ in [0] * N]

ALL = 1 << N


def has_bit(n, i):
    return n & (1 << i) > 0


ans = 10
for n in range(ALL):
    flag = [0] * M
    for i in range(N):
        if has_bit(n, i):
            for j in range(M):
                if S[i][j] == "o":
                    flag[j] = 1
    if sum(flag) == M:
        ans = min(ans, n.bit_count())

print(ans)
