from sys import stdin

readline = stdin.readline
s = int(readline())
mod = 10 ** 9 + 7
a = [0] * (s + 1)
a[0] = 1
for i in range(3, s + 1):
    a[i] = a[i - 1] + a[i - 3]
    a[i] %= mod

print(a[s])
