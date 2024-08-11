N = int(input())
S = [input() for _ in [0] * N]

M = max(len(s) for s in S)
S = [s + "*" * (M - len(s)) for s in S]
S = S[::-1]

S = list(zip(*S))

for s in S:

    for i in range(len(s)):
        if s[i] != "*":
            last = i
    print(*s[: last + 1], sep="")
