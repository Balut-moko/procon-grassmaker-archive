from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
ans = 1
for i in range(b - a, 0, -1):
    if 2 <= (b // i) - ((a - 1) // i):
        ans = i
        break
print(ans)
