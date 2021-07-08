from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
p = [tuple(map(int, readline().split())) for _ in [0] * h]
ans = 0
for i in range(1, 2**h):
    r = []
    c = dict()
    cnt = 0
    for j in range(h):
        if (i >> j) & 1:
            r.append(j)
            cnt += 1
    for a in range(w):
        tmp = p[r[0]][a]
        for b in r:
            if tmp != p[b][a]:
                break
        else:
            if tmp not in c:
                c[tmp] = 1
            else:
                c[tmp] += 1
            continue
    while c:
        key, val = c.popitem()
        ans = max(ans, cnt * val)
print(ans)