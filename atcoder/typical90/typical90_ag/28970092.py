from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
if h == 1 or w == 1:
    ans = h * w
else:
    ans = ((h + 1) // 2) * ((w + 1) // 2)
print(ans)
