from sys import stdin
import math

readline = stdin.readline
a, b, d = map(int, readline().split())
th = math.radians(d)
aa = a * math.cos(th) - b * math.sin(th)
bb = a * math.sin(th) + b * math.cos(th)
print(aa, bb)
