from sys import stdin

readline = stdin.readline
n = int(readline())
p = [0, 1] + list(map(int, readline().split()))

ans = 0
now = n
while now != 1:
    ans += 1
    now = p[now]
print(ans)
