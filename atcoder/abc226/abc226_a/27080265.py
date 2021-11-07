from sys import stdin

readline = stdin.readline
i, x = map(int, readline().split('.'))
if x < 500:
    print(i)
else:
    print(i + 1)
