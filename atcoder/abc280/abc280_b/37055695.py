from sys import stdin

readline = stdin.readline
n = int(readline())
s = [0] + list(map(int, readline().split()))
ans = [0] * n

for i in range(n):
    ans[i] = s[i + 1] - s[i]

print(*ans)
