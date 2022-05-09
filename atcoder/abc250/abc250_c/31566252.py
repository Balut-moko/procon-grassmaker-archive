from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())
a = [i for i in range(1, n + 1)]
a_di = {v: i for i, v in enumerate(a)}
for _ in range(q):
    x = int(readline())
    idx = a_di[x]
    if idx == n - 1:
        right = n - 2
    else:
        right = idx + 1
    tmp = a[right]
    a[right] = x
    a[idx] = tmp
    a_di[x] = right
    a_di[tmp] = idx

print(*a)
