from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

ab.sort()
cnt = 0
for a, b in ab:
    cnt += b
ans = 1
if cnt <= k:
    print(1)
    exit()

for i in range(n):
    a, b = ab[i]
    cnt -= b
    ans = a + 1
    if cnt <= k:
        break
print(ans)
