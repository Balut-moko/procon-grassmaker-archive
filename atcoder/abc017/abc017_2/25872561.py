from sys import stdin

readline = stdin.readline
x = readline()[:-1]
i = 0
while i < len(x):
    if x[i] in {'o', 'k', 'u'}:
        i += 1
        continue
    if i < len(x) - 1:
        if x[i] == 'c' and x[i + 1] == 'h':
            i += 2
            continue
    print('NO')
    exit()
print('YES')
