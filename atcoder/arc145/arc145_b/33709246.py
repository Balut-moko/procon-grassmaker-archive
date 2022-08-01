from sys import stdin

readline = stdin.readline
n, a, b = map(int, readline().split())
if n < a:
    ans = 0
else:
    ans = n // a * min(a, b) + min(n % a, b - 1)
    ans -= min(a - 1, b - 1)
print(ans)
