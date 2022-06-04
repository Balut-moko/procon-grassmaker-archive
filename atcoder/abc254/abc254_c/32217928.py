from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))

group = [[] for _ in range(k)]

for i in range(n):
    group[i % k].append(a[i])

group = [sorted(val) for val in group]
pre = 0
for j in range(len(group[0])):
    for i in range(k):
        if len(group[i]) == j:
            break
        if group[i][j] < pre:
            print("No")
            exit()
        pre = group[i][j]
    else:
        continue
    break
print("Yes")
