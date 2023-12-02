from collections import defaultdict


N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in [0] * L]
dct = defaultdict(set)
for c, d in CD:
    dct[c].add(d)

BB = [(v, i) for i, v in enumerate(B)]
BB.sort(reverse=True)

ans = 0
for i in range(N):
    tmp = A[i]
    for v, j in BB:
        if j not in dct[i]:
            ans = max(ans, A[i] + v)
            break

print(ans)
