from sys import stdin
import math


def calc_angle(a, b):
    return math.degrees(math.atan2(b, a))


readline = stdin.readline
t = int(readline())
l, x, y = map(int, readline().split())
q = int(readline())
for _ in range(q):
    e = int(readline())
    p = math.radians(360 * e / t)
    y1 = -math.sin(p) * l / 2
    z1 = l / 2 - math.cos(p) * l / 2
    a = math.sqrt(x * x + (y - y1) * (y - y1))
    print(calc_angle(a, z1))
