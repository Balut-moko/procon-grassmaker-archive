from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

cnt0 = [0] * 60
cnt1 = [0] * 60

for i in range(n):
    for j in range(60):
        if (a[i] >> j) & 1:
            cnt1[j] += 1
        else:
            cnt0[j] += 1

ans = 0
mod = 10**9 + 7
for i in range(n):
    for j in range(60):
        if (a[i] >> j) & 1:
            cnt1[j] -= 1
            ans += 2**j * cnt0[j]
            ans %= mod
        else:
            cnt0[j] -= 1
            ans += 2**j * cnt1[j]
            ans %= mod

print(ans)
