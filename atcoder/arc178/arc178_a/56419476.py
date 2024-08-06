N, M = map(int, input().split())
A = list(map(int, input().split()))

b = [0] * N
for a in A:
    b[a - 1] = 1

if b[0] or b[N - 1]:
    print(-1)
    exit()

P = [0] * N
P[0] = 1
a = 2

for i in range(1, N):
    if b[i] == 1:
        P[i] = i + 2
    else:
        P[i] = a
        a = i + 2

print(*P)
