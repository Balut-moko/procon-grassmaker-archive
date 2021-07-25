from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
ck = []
mod = 998244353
cnt = k
for i in range(k):
    c, num = readline().split()
    ck.append([int(num) - 1, c])
    if c == 'L':
        cnt -= 1
ck.sort()
now = 0
ans = 1
for i in range(n):
    if now < k and i == ck[now][0]:
        if ck[now][1] == 'L':
            cnt += 1
        else:
            cnt -= 1
        now += 1
    else:
        ans *= cnt
        ans %= mod
print(ans)
