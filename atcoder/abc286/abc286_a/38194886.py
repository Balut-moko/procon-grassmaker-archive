from sys import stdin

readline = stdin.readline
n, p, q, r, s = map(int, readline().split())
a = list(map(int, readline().split()))

ans = a[: p - 1] + a[r - 1 : s] + a[q : r - 1] + a[p - 1 : q] + a[s:]
# + a[r - 1 : s - 2] + a[q - 1 : r - 1] + a[p - 1 : q - 1] + a[s - 1 :]

print(*ans)
