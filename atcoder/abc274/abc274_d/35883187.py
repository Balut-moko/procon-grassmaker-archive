from sys import stdin

readline = stdin.readline
n, x, y = map(int, readline().split())
a = list(map(int, readline().split()))

x_set = {a[0]}
y_set = {0}

for i in range(1, n):
    if i % 2 == 0:
        tmp = set()
        for val in x_set:
            tmp.add(val + a[i])
            tmp.add(val - a[i])
        x_set = tmp
    else:
        tmp = set()
        for val in y_set:
            tmp.add(val + a[i])
            tmp.add(val - a[i])
        y_set = tmp

if x in x_set and y in y_set:
    ans = "Yes"
else:
    ans = "No"
print(ans)
