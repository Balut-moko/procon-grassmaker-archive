from sys import stdin

readline = stdin.readline
n, a, b = map(int, readline().split())
if n == 1:
    if a == b:
        ans = 1
    else:
        ans = 0
else:
    ans = (a + b * (n - 1)) - (a * (n - 1) + b) + 1
    ans = max(ans, 0)
print(ans)
