from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
ans = (0, 0)
for i in range(1, 10):
    x = 0
    for j in range(1, n + 1):
        x = (10 * x + i) % m
        if x == 0:
            ans = max(ans, (j, i))
j, i = ans
if ans == (0, 0):
    print(-1)
else:
    ans = int(str(i) * j)
    print(ans)
