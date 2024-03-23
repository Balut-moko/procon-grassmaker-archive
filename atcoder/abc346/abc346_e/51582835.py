from collections import defaultdict


H, W, M = map(int, input().split())

que = [tuple(map(int, input().split())) for _ in [0] * M]

que = que[::-1]

rows = {r + 1 for r in range(H)}
cols = {c + 1 for c in range(W)}

ans_di = defaultdict(int)
color = set()
for m in range(M):
    t, a, x = que[m]
    x += 1
    if t == 1:  # row
        if a in rows:
            ans_di[x] += len(cols)
            rows.discard(a)
            color.add(x)
    if t == 2:  # col
        if a in cols:
            ans_di[x] += len(rows)
            cols.discard(a)
            color.add(x)

ans_di[1] += len(rows) * len(cols)
if ans_di[1] != 0:
    color.add(1)
for k, v in sorted(ans_di.items()):
    if v == 0:
        color.discard(k)

print(len(color))
for k, v in sorted(ans_di.items()):
    if v != 0:
        print(k - 1, v)
