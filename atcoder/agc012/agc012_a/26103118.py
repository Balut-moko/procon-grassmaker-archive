from sys import stdin

readline = stdin.readline
n = int(readline())
a = sorted(map(int, readline().split()), reverse=True)
ans = 0
for i in range(n):
    ans += a[i * 2 + 1]
print(ans)
