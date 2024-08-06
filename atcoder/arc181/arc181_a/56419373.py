from operator import index


T = int(input())

for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    if P == list(range(1, N + 1)):
        print(0)
        continue
    if P[0] == N and P[-1] == 1:
        print(3)
        continue
    mx = 0
    ans = 2
    for i in range(N):
        mx = max(mx, P[i])
        if mx == i + 1 and P[i] == i + 1:
            ans = 1
    print(ans)
