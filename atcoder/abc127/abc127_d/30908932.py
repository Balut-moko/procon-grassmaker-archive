from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
bc = [tuple(map(int, readline().split())) for _ in [0] * m]

for val in a:
    bc.append((1, val))

bc.sort(reverse=True, key=lambda x: x[1])
ans = 0
for b, c in bc:
    if b < n:
        ans += b * c
        n -= b
    else:
        ans += n * c
        break

print(ans)
