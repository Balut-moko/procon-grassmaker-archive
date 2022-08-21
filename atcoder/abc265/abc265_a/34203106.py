from sys import stdin

readline = stdin.readline
x, y, n = map(int, readline().split())

if 3 * x <= y:
    ans = n * x
else:
    div, mod = divmod(n, 3)
    ans = div * y + mod * x
print(ans)
