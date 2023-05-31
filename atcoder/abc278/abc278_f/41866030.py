from sys import stdin

readline = stdin.readline
N = int(readline())
S = [readline()[:-1] for _ in range(N)]


def has_bit(n, i):
    return n & (1 << i) > 0


ALL = 1 << N
dp = [[False] * 26 for _ in [0] * ALL]

for n in range(1, ALL):
    for i in range(N):
        if has_bit(n, i):
            if not dp[n - (1 << i)][ord(S[i][-1]) - 97]:
                dp[n][ord(S[i][0]) - 97] = True

print("First" if any(dp[-1]) else "Second")
