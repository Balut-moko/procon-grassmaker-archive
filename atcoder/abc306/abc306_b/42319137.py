from sys import stdin

readline = stdin.readline
a = list(map(int, readline().split()))

ans = 0

for i, val in enumerate(a):
    ans += val * 2 ** i

print(ans)
