from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
mod = 10 ** 9 + 7
for i in range(n):
    a[i] += 1

cnt = [0] * (n + 1)
cnt[0] = 3

ans = 1
for i in range(n):
    if 0 < cnt[a[i] - 1]:
        ans *= cnt[a[i] - 1]
        ans %= mod
        cnt[a[i] - 1] -= 1
        cnt[a[i]] += 1
        continue
    ans = 0
    break

print(ans)
