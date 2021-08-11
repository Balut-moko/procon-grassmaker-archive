from sys import stdin

readline = stdin.readline
n = int(readline())
ans = [0] * 6
for _ in range(n):
    t = list(map(float, readline().split()))
    if 35 <= t[0]:
        ans[0] += 1
    if 30 <= t[0] < 35:
        ans[1] += 1
    if 25 <= t[0] < 30:
        ans[2] += 1
    if 25 <= t[1]:
        ans[3] += 1
    if 0 <= t[0] and t[1] < 0:
        ans[4] += 1
    if t[0] < 0:
        ans[5] += 1

print(*ans)
