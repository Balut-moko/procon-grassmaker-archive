from sys import stdin

readline = stdin.readline
x, y, z = map(int, readline().split())
for i in range(1000001):
    if i * x < y * z:
        ans = i
print(ans)
