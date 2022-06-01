from sys import stdin

readline = stdin.readline
n = int(readline())
arms = []

for _ in range(n):
    x, l = map(int, readline().split())
    arm = (x - l, x + l)
    arms.append(arm)

arms.sort(key=lambda x: x[1])

ans = 0
cur = -1 << 60

for l, r in arms:
    if cur <= l:
        ans += 1
        cur = r
print(ans)
