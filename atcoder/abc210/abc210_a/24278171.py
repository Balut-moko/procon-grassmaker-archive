from sys import stdin

readline = stdin.readline
n, a, x, y = map(int, readline().split())
if a < n:
    ans = a * x + (n - a) * y
else:
    ans = n * x
print(ans)
