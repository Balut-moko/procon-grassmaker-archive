from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in [0] * h]
b = [list(map(int, readline().split())) for _ in [0] * h]
ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        tmp = b[i][j] - a[i][j]
        ans += abs(tmp)
        a[i][j] += tmp
        a[i + 1][j] += tmp
        a[i][j + 1] += tmp
        a[i + 1][j + 1] += tmp
if a == b:
    print('Yes')
    print(ans)
else:
    print('No')
