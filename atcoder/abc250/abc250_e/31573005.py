from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
q = int(readline())
query = [tuple(map(int, readline().split())) for _ in [0] * q]

a_idx_di = {v: n - i - 1 for i, v in enumerate(a[::-1])}
b_idx_di = {v: n - i - 1 for i, v in enumerate(b[::-1])}

ab_idx_li = [0] * (n + 1)
for i, val in enumerate(a):
    idx = b_idx_di.get(val, n)
    ab_idx_li[i + 1] = max(ab_idx_li[i], idx)

ba_idx_li = [0] * (n + 1)
for i, val in enumerate(b):
    idx = a_idx_di.get(val, n)
    ba_idx_li[i + 1] = max(ba_idx_li[i], idx)

for x, y in query:
    yy = ab_idx_li[x]
    xx = ba_idx_li[y]
    if xx < x and yy < y:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
