from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))

cs = [0] * (n + 1)
cs[0] = 0
pre = [-1] * (n + 1)
pre[0] = 0

for i in range(n):
    cs[i + 1] = cs[i] + a[cs[i] % n]
    if pre[cs[i + 1] % n] != -1:
        s = pre[cs[i + 1] % n]
        t = i + 1
        break
    pre[cs[i + 1] % n] = i + 1

if k <= s:
    ans = cs[k]
else:
    p = t - s
    cycle = cs[t] - cs[s]
    div, mod = divmod(k - s - 1, p)
    ans = cs[s + mod + 1] + div * cycle
print(ans)
