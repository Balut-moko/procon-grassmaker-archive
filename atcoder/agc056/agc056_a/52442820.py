N = int(input())
S = []
for i in range(N):
    s = ["."] * N
    for j in range(3):
        s[(i * 3 + j) % N] = "#"
    S.append(s)
if N % 3 != 0:
    S[0], S[N // 3 - 1] = S[N // 3 - 1], S[0]
    S[N - N // 3], S[N - 1] = S[N - 1], S[N - N // 3]

for s in S:
    print(*s, sep="")
