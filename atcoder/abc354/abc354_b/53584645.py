N = int(input())
A = [input().split() for _ in [0] * N]
A.sort()
T = 0

for i in range(N):
    T += int(A[i][1])

print(A[T % N][0])
