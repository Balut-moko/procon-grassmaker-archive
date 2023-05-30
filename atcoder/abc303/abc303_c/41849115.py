from sys import stdin

readline = stdin.readline
n, m, h, k = map(int, readline().split())
s = readline()[:-1]
xy = {tuple(map(int, readline().split())) for _ in [0] * m}

x, y = 0, 0

for i in range(n):
    h -= 1
    if s[i] == "R":
        x += 1
    if s[i] == "L":
        x -= 1
    if s[i] == "U":
        y += 1
    if s[i] == "D":
        y -= 1
    if h < 0:
        print("No")
        exit()
    if h < k and (x, y) in xy:
        h = k
        xy.discard((x, y))
print("Yes")
