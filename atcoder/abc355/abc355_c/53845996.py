N, T = map(int, input().split())
A = list(map(int, input().split()))

row = [0] * N
col = [0] * N
x1 = 0
x2 = 0

for t in range(T):
    a = A[t]
    a -= 1
    j = a % N
    a -= j
    i = a // N

    row[i] += 1
    col[j] += 1
    if i == j:
        x1 += 1
    if i + j == N - 1:
        x2 += 1
    if max(row[i], col[j], x1, x2) == N:
        print(t + 1)
        exit()
print(-1)
