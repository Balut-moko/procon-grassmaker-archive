from sys import stdin

readline = stdin.readline
n = int(readline())
h = list(map(int, readline().split()))
ans = h[0]
for i in range(1, n):
    if h[i] > ans:
        ans = h[i]
    else:
        break
print(ans)
