from sys import stdin

readline = stdin.readline
n = int(readline())
t = readline()[:-1]
pos = [0, 0]
dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
angle = 1
for i in range(n):
    if t[i] == "S":
        pos[0] += dxy[angle][0]
        pos[1] += dxy[angle][1]
    else:
        angle += 1
        angle %= 4
print(*pos)
