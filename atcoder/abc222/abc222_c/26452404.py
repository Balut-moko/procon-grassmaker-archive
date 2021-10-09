from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = [[0, i + 1, i + 1] + list(readline()[:-1]) for i in range(n * 2)]
ans = 0
for j in range(m):
    for i in range(0, n * 2, 2):
        if a[i][j + 3] == 'G':
            if a[i + 1][j + 3] == 'G':
                pass
            elif a[i + 1][j + 3] == 'C':
                a[i][0] -= 1
            else:
                a[i + 1][0] -= 1
        elif a[i][j + 3] == 'C':
            if a[i + 1][j + 3] == 'G':
                a[i + 1][0] -= 1
            elif a[i + 1][j + 3] == 'C':
                pass
            else:
                a[i][0] -= 1
        else:
            if a[i + 1][j + 3] == 'G':
                a[i][0] -= 1
            elif a[i + 1][j + 3] == 'C':
                a[i + 1][0] -= 1
            else:
                pass
    a = sorted(a)
    for i in range(n * 2):
        a[i][2] = i + 1

for i in range(n * 2):
    print(a[i][1])
