from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
cells = [0, 0, 0, 0]
p = 0
for i in range(n):
    cells[0] = 1
    for j in range(3, -1, -1):
        if a[i] + j > 3:
            p += cells[j]
        else:
            cells[a[i] + j] = cells[j]
        cells[j] = 0
print(p)
