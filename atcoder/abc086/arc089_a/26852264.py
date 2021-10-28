from sys import stdin

readline = stdin.readline
n = int(readline())
now = 0
x, y = 0, 0
for _ in range(n):
    t, nx, ny = map(int, readline().split())
    if (t % 2) + (nx + ny) % 2 != 1:
        if abs(nx - x) + abs(ny - y) <= t - now:
            now = t
            x, y = nx, ny
            continue
    print('No')
    exit()
print('Yes')
