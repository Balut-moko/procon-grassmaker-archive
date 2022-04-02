from sys import stdin

readline = stdin.readline
x1, y1 = map(int, readline().split())
x2, y2 = map(int, readline().split())
x3, y3 = map(int, readline().split())

if x1 == x2:
    x = x3
elif x1 == x3:
    x = x2
else:
    x = x1

if y1 == y2:
    y = y3
elif y1 == y3:
    y = y2
else:
    y = y1

print(x, y)
