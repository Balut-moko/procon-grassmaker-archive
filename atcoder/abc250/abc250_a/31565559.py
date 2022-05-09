from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
r, c = map(lambda x: int(x) - 1, readline().split())
dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
ans = 0
for dr, dc in dd:
    if 0 <= r + dr < h and 0 <= c + dc < w:
        ans += 1
print(ans)
