from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]
x_set = set()
x_set.add(0)

for a, b in ab:
    x_li = list(x_set)
    x_set.clear()
    for val in x_li:
        x_set.add(val + a)
        x_set.add(val + b)
if x in x_set:
    ans = "Yes"
else:
    ans = "No"
print(ans)
