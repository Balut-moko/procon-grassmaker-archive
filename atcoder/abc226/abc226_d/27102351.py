from sys import stdin
import math

readline = stdin.readline
n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in [0] * n]
dist_set = set()
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dist_x = xy[i][0] - xy[j][0]
        dist_y = xy[i][1] - xy[j][1]
        if dist_x == 0:
            if dist_y < 0:
                dist_set.add((0, -1))
            else:
                dist_set.add((0, 1))
        elif dist_y == 0:
            if dist_x < 0:
                dist_set.add((-1, 0))
            else:
                dist_set.add((1, 0))
        else:
            a = math.gcd(dist_x, dist_y)
            dist = (dist_x // a, dist_y // a)
            dist_set.add(dist)
print(len(dist_set))
