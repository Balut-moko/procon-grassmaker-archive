from sys import stdin

readline = stdin.readline
m = int(readline())
d = list(map(int, readline().split()))

h = sum(d) // 2 + 1
for i in range(m):
    for j in range(d[i]):
        h -= 1
        if h == 0:
            print(i + 1, j + 1)
