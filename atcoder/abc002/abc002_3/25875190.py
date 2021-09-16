from sys import stdin

readline = stdin.readline
xy = list(map(int, readline().split()))
xy[2] -= xy[0]
xy[3] -= xy[1]
xy[4] -= xy[0]
xy[5] -= xy[1]
xy[0], xy[1] = 0, 0
print(abs(xy[2] * xy[5] - xy[3] * xy[4]) / 2)
