from sys import stdin

readline = stdin.readline
n = int(readline())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

sum_seconds = sum([a / b for a, b in ab])
half = sum_seconds / 2
ans = 0
for a, b in ab:
    if a / b <= half:
        ans += a
        half -= a / b
    else:
        ans += half * b
        break
print(ans)
