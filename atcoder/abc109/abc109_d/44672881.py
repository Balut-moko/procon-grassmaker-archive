from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in [0] * h]

ans = []

for r in range(h):
    for c in range(w - 1):
        if a[r][c] % 2 == 1:
            ans.append((r, c, r, c + 1))
            a[r][c] -= 1
            a[r][c + 1] += 1

for r in range(h - 1):
    if a[r][w - 1] % 2 == 1:
        ans.append((r, w - 1, r + 1, w - 1))
        a[r][w - 1] -= 1
        a[r + 1][w - 1] += 1

print(len(ans))
for val in ans:
    val = list(map(lambda x: x + 1, val))
    print(*val)
