N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_set = set(A)

C = sorted(A + B)
flag = False
for i in range(N + M - 1):
    if C[i] in A_set and C[i + 1] in A_set:
        flag = True

print("Yes" if flag else "No")
