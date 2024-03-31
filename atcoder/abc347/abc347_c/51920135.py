N, A, B = map(int, input().split())
D = list(map(int, input().split()))

week = A + B
DD = sorted(d % week for d in D)

flag = False
mn = DD[0]
mx = DD[-1]
if mx - mn < A:
    flag = True

for i in range(1, N):
    mn = DD[i]
    mx = DD[(N - 1 + i) % N] + week
    if mx - mn < A:
        flag = True

print("Yes" if flag else "No")
