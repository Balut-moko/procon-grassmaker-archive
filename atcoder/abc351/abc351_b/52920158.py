from itertools import product


N = int(input())
A = [input() for _ in [0] * N]
B = [input() for _ in [0] * N]

for i, j in product(range(N), repeat=2):
    if A[i][j] != B[i][j]:
        print(i + 1, j + 1)
