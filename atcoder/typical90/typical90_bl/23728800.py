from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())
a = list(map(int, readline().split()))
b = [0] * (n - 1)
ans = 0
for i in range(n - 1):
    b[i] += a[i + 1] - a[i]
    ans += abs(b[i])

for _ in [0] * q:
    left, right, v = map(int, readline().split())
    pre = 0
    after = 0
    if left != 1:
        pre += abs(b[left - 2])
        b[left - 2] += v
        after += abs(b[left - 2])
    if right != n:
        pre += abs(b[right - 1])
        b[right - 1] -= v
        after += abs(b[right - 1])
    ans += after - pre
    print(ans)
