N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [tuple(map(int, input().split())) for _ in [0] * N]
X_transpose = list(zip(*X))

flag = True
for i in range(M):
    if sum(X_transpose[i]) < A[i]:
        flag = False

print("Yes" if flag else "No")
