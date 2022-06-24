from sys import stdin


def f(x):
    xx = x[::-1]
    xx = str(int(xx))
    return xx


readline = stdin.readline
n, k = readline().split()
n = int(n)
ans_set = set()

for i in range(20):
    x = k + "0" * i
    if not (1 <= int(x) <= n):
        break
    if x == k:
        ans_set.add(x)
    xx = f(x)
    if xx == k:
        ans_set.add(x)
    xx = f(xx)
    if xx == k:
        ans_set.add(x)
for i in range(20):
    xr = f(k) + "0" * i
    if not (1 <= int(xr) <= n):
        break
    xxr = f(xr)
    if xxr == k:
        ans_set.add(xr)
    xxr = f(xxr)
    if xxr == k:
        ans_set.add(xr)

if len(ans_set) == 0:
    print(0)
    exit()

if min(ans_set) != k:
    print(0)
    exit()
print(len(ans_set))
