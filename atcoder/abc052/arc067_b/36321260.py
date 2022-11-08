from sys import stdin

readline = stdin.readline
n, a, b = map(int, readline().split())
x = list(map(int, readline().split()))
ans = 0
for i in range(1, n):
    if (x[i] - x[i - 1]) * a <= b:
        ans += (x[i] - x[i - 1]) * a
    else:
        ans += b
print(ans)
