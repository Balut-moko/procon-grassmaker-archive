from sys import stdin

readline = stdin.readline
n = int(readline())
lst = []
min_a = 1 << 60
for _ in range(n):
    s, a = readline().split()
    a = int(a)
    min_a = min(min_a, a)
    lst.append((s, a))

for i in range(n):
    if lst[i][1] == min_a:
        idx = i

lst = lst[idx:] + lst[:idx]

for s, _ in lst:
    print(s)
