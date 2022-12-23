from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())

if k == 0:
    print(n * n)
    exit()

ans = 0
for b in range(k + 1, n + 1):
    nn = (n + 1) // b
    d = 0
    d += (b - k) * nn

    left = k + b * nn
    right = n
    if left <= right:
        d += right - left + 1
    ans += d
print(ans)
