from bisect import bisect_right
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
H = list(map(int, readline().split()))
W = list(map(int, readline().split()))
H.sort()
ep = [0]
op = []

for i in range(n - 1):
    if i % 2 == 0:
        ep.append(H[i + 1] - H[i])
    else:
        op.append(H[i + 1] - H[i])
op.append(0)

for i in range(len(ep) - 1):
    ep[i + 1] += ep[i]
for i in range(len(op) - 1, 0, -1):
    op[i - 1] += op[i]

ans = 1 << 60
for w in W:
    idx = bisect_right(H, w)
    if idx % 2:
        idx -= 1
    tmp = ep[idx // 2] + op[idx // 2] + abs(H[idx] - w)
    ans = min(ans, tmp)
print(ans)
