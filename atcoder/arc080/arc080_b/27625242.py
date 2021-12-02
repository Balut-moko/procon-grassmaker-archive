from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
n = int(readline())
a = list(map(int, readline().split()))
color = []
for i, val in enumerate(a):
    color += [i + 1] * val
ans = [color[i:i + w] for i in range(0, len(color), w)]
for i in range(h):
    if i % 2 == 0:
        print(*ans[i])
    else:
        print(*ans[i][::-1])
