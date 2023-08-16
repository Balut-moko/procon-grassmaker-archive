from sys import stdin

readline = stdin.readline
N = int(readline())

for h in range(1, 3501):
    for n in range(1, 3501):
        if 4 * h * n - N * n - N * h == 0:
            continue
        w = N * h * n // (4 * h * n - N * n - N * h)
        if w < 0:
            continue
        if 4 * h * n * w == N * (n * w + h * w + h * n):
            print(h, n, w)
            exit()
