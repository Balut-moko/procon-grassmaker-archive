from sys import stdin

readline = stdin.readline
a, b, c = map(int, readline().split())
i = 1
while c * i <= b:
    if a <= c * i <= b:
        print(c * i)
        exit()
    i += 1
print(-1)
