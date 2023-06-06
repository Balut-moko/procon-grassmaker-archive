from sys import stdin


def f(x):
    if x < 7:
        return -1
    for i in range(60, -1, -1):
        if x <= 2 ** i:
            continue
        for j in range(i - 1, -1, -1):
            if x <= 2 ** i + 2 ** j:
                continue
            for k in range(j - 1, -1, -1):
                if 2 ** i + 2 ** j + 2 ** k <= x:
                    return 2 ** i + 2 ** j + 2 ** k


readline = stdin.readline
t = int(readline())

for _ in range(t):
    print(f(int(readline())))
