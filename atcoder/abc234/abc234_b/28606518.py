from sys import stdin

readline = stdin.readline
n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in [0] * n]
ans = 0
for x1, y1 in xy:
    for x2, y2 in xy:
        ans = max(ans, (x1 - x2)**2 + (y1 - y2)**2)

print(ans**0.5)
