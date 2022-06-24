from sys import stdin


def f(x):
    xx = int(str(x)[::-1])
    xx = min(xx, int(str(xx)[::-1]))
    return xx


readline = stdin.readline
n, k = map(int, readline().split())
ans_set = set()

for i in range(13):
    x = k * (10 ** i)
    if not (1 <= x <= n):
        break
    if f(x) == k:
        ans_set.add(x)

kr = int(str(k)[::-1])
for i in range(13):
    x = kr * (10 ** i)
    if not (1 <= x <= n):
        break
    if f(x) == k:
        ans_set.add(x)

print(len(ans_set))
