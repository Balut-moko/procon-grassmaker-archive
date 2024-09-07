N = int(input())
A = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in [0] * N]
i = 0
for j in range(N):
    if i >= j:
        i = A[i][j]
    else:
        i = A[j][i]

print(i + 1)
