from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = sorted(map(int, readline().split()), reverse=True) + [0]
fun = 0
for i in range(n):
    tmp = a[i] - a[i + 1]
    if (i + 1) * tmp <= k:
        fun += (i + 1) * ((a[i] * (a[i] + 1)) // 2 - (a[i + 1] * (a[i + 1] + 1)) // 2)
        k -= (i + 1) * tmp
    else:
        cnt = k // (i + 1)
        fun += (i + 1) * ((a[i] * (a[i] + 1)) // 2 - ((a[i] - cnt) * (a[i] - cnt + 1)) // 2)
        k %= i + 1
        fun += k * (a[i] - cnt)
        break
print(fun)
