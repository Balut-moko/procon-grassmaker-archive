from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
ab = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * m]

ab.sort(key=lambda x: x[1])

ans = 0
pre = -1
for a, b in ab:
    if a < pre:
        continue
    ans += 1
    pre = b

print(ans)
