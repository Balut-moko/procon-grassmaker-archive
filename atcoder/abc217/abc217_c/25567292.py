from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
ans = [0] * n
for i, p in enumerate(a):
    ans[p - 1] = i + 1
print(*ans)
