from sys import stdin

readline = stdin.readline
c = [tuple(map(int, readline().split())) for _ in [0] * 3]
for k in range(-100, 101):
    tmp = c[0][0] - k
    a = [0] * 3
    a = [k, c[1][0] - tmp, c[2][0] - tmp]
    b = [tmp, c[0][1] - k, c[0][2] - k]
    for i in range(3):
        for j in range(3):
            if a[i] + b[j] != c[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
print('No')
