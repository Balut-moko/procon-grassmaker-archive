N, Q = map(int, input().split())
x = list(map(lambda x: int(x) - 1, input().split()))
A = [0] * N
S = set()
len_cum = [0]
cnt = 0
idx = [-1] * N
for i, v in enumerate(x):
    if v in S:
        A[v] += len_cum[-1] - len_cum[idx[v]]
        S.discard(v)
        cnt -= 1
    else:
        idx[v] = i
        S.add(v)
        cnt += 1
    len_cum.append(len_cum[-1] + cnt)

for v in S:
    A[v] += len_cum[-1] - len_cum[idx[v]]
print(*A)
