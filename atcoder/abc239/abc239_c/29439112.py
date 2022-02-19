from sys import stdin

readline = stdin.readline
x1, y1, x2, y2 = map(int, readline().split())
dxy = ((-2, 1), (2, -1), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
ans = "No"
for dx1, dy1 in dxy:
    for dx2, dy2 in dxy:
        if x1 + dx1 == x2 + dx2 and y1 + dy1 == y2 + dy2:
            ans = "Yes"

print(ans)
