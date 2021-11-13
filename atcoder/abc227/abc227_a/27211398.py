from sys import stdin

readline = stdin.readline
n, k, a = map(int, readline().split())
ans = 0
k = k % n
ans = (k + a - 1) % n
if ans == 0:
    ans = n
print(ans)
