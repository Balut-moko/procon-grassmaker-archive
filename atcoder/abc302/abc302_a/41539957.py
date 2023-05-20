from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
at = a//b
a -= at*b
if a == 0:
    print(at)
else:
    print(at+1)
