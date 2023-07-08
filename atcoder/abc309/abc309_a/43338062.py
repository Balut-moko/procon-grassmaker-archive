from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
if a > b:
    a, b = b, a
flag = False
if (a, b) in ((1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 9)):
    flag = True
print("Yes" if flag else "No")
