from sys import stdin

readline = stdin.readline
n = int(readline())
fs = [tuple(map(int, readline().split())) for _ in [0] * n]
s_max = 0
idx = -1
for i in range(n):
    if s_max <= fs[i][1]:
        s_max = fs[i][1]
        idx = i
ans = 0
for i in range(n):
    if idx == i:
        continue
    if fs[i][0] == fs[idx][0]:
        ans = max(ans, s_max + fs[i][1] // 2)
    else:
        ans = max(ans, s_max + fs[i][1])

print(ans)
