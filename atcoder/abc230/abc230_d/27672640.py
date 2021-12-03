from sys import stdin

readline = stdin.readline
n, d = map(int, readline().split())
lr = sorted([tuple(map(int, readline().split())) for _ in [0] * n], key=lambda x: x[1])
x = -(1 << 60)
ans = 0
for l, r in lr:
    if x + d - 1 < l:
        ans += 1
        x = r
print(ans)
