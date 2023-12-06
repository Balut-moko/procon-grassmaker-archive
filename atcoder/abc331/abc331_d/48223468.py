N, Q = map(int, input().split())
P = [input() for _ in [0] * N]

black = [[0] * (N + 1) for _ in range(N + 1)]


def f(H, W):
    if H <= N and W <= N:
        return black[H][W]
    Hd, Hm = divmod(H, N)
    Wd, Wm = divmod(W, N)
    ret = 0
    ret += f(N, N) * Hd * Wd
    ret += f(Hm, N) * Wd
    ret += f(N, Wm) * Hd
    ret += f(Hm, Wm)
    return ret


def calc(A, B, C, D):
    return f(C, D) - f(A, D) - f(C, B) + f(A, B)


for i in range(1, N + 1):
    for j in range(1, N + 1):
        if P[i - 1][j - 1] == "B":
            black[i][j] += 1
        black[i][j] += black[i - 1][j]
        black[i][j] += black[i][j - 1]
        black[i][j] -= black[i - 1][j - 1]

for _ in range(Q):
    A, B, C, D = map(int, input().split())
    print(calc(A, B, C + 1, D + 1))
