from sys import stdin

readline = stdin.readline
n, h = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

ab = sorted(ab, reverse=True, key=lambda x: x[1])
a_max = 0
a_max_idx = 0
for i, val in enumerate(ab):
    if a_max <= val[0]:
        a_max = max(a_max, val[0])
        a_max_idx = i

ans = 0
for i, val in enumerate(ab):
    if a_max <= val[1]:
        h -= val[1]
        ans += 1
        if h <= 0:
            print(ans)
            exit()


div, mod = divmod(h, a_max)
ans += div
if mod != 0:
    ans += 1
print(ans)
