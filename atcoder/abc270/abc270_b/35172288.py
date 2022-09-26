from sys import stdin

readline = stdin.readline
x, y, z = map(int, readline().split())

if y < 0:
    x = -x
    y = -y
    z = -z
if x < y:
    print(abs(x))
else:
    if y < z:
        print(-1)
    else:
        print(abs(z) + abs(x - z))

