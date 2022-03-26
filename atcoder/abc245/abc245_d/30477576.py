from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
c = list(map(int, readline().split()))
b = [0] * (m + 1)

j = m
while j >= 0:
    for k in range(-100, 101):
        if c[n + j] == a[n] * k:
            b[j] = k
            break
    for k in range(n + 1):
        c[k + j] -= a[k] * b[j]
    j -= 1

print(*b)
