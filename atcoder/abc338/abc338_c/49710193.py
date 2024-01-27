N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for a in range(10**6 + 1):
    C = [0] * N
    D = [0] * N
    flag = False
    for j in range(N):
        C[j] += A[j] * a
        if Q[j] < C[j]:
            flag = True
            break
    if flag:
        continue
    for j in range(N):
        if B[j] == 0:
            D[j] = 1 << 60
        else:
            D[j] = (Q[j] - C[j]) // B[j]
    ans = max(ans, a + min(D))

print(ans)
