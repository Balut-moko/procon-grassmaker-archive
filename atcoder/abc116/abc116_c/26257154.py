from sys import stdin

readline = stdin.readline
n = int(readline())
h = list(map(int, readline().split()))
ans = h[0]
for i in range(n - 1):
    if h[i + 1] - h[i] > 0:
        ans += h[i + 1] - h[i]
print(ans)
