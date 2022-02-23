from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in [0] * h]
b = [list(map(int, readline().split())) for _ in [0] * h]
cnt = 0
for i in range(h - 1):
    for j in range(w - 1):
        dif = b[i][j] - a[i][j]
        a[i][j] += dif
        a[i][j + 1] += dif
        a[i + 1][j] += dif
        a[i + 1][j + 1] += dif
        cnt += abs(dif)
if a == b:
    print("Yes")
    print(cnt)
else:
    print("No")
