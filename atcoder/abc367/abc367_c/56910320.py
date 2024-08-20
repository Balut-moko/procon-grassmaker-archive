from sympy import Q


N, K = map(int, input().split())
R = list(map(lambda x: int(x) + 1, input().split()))

ans = []
ans.append([])
for i in range(N):
    tmp = []
    for v in ans:
        for j in range(1, R[i]):
            t = v[:]
            t.append(j)
            tmp.append(t)
    ans = tmp

for v in ans:
    if sum(v) % K == 0:
        print(*v)
