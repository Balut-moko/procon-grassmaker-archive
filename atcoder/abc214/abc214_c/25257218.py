from sys import stdin

readline = stdin.readline
n = int(readline())
s = list(map(int, readline().split()))
t = list(map(int, readline().split()))
s = s + s
t = t + t
ans = [0] * (n * 2)
ans[0] = t[0]
for i in range(1, n * 2):
    ans[i] = min(ans[i - 1] + s[i - 1], t[i])
for i in range(n):
    ans[i] = min(ans[i], ans[i + n])
print(*ans[:n], sep='\n')
