from sys import stdin

readline = stdin.readline
n = int(readline())
x = []
y = []
for i in range(n):
    i, j = map(int, readline().split())
    x.append(i)
    y.append(j)

x_sorted = sorted(x)
y_sorted = sorted(y)
x_median = x_sorted[n // 2]
y_median = y_sorted[n // 2]
ans = 0
for i in range(n):
    ans += abs(x[i] - x_median) + abs(y[i] - y_median)
print(ans)
