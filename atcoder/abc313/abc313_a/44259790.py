from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))

if n == 1:
    print(0)
    exit()

ans = 0
tmp = max(p[1:])


if p[0] <= tmp:
    ans = tmp - p[0] + 1

print(ans)
