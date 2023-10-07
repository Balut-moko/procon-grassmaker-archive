N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in [0] * N]

points = [i + 1 for i in range(N)]
AA = [(v, i) for i, v in enumerate(A)]
AA.sort(reverse=True)

for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            points[i] += A[j]

first = max(points)

ans = [0] * N

for i in range(N):
    now = points[i]
    if now == first:
        continue
    for v, j in AA:
        if S[i][j] == "o":
            continue
        now += v
        ans[i] += 1
        if first < now:
            break

print(*ans, sep="\n")
