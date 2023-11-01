from collections import deque


T = int(input())


def check(x, y):
    cnt_a = y.count("A") - x.count("A")
    cnt_b = y.count("B") - x.count("B")

    if cnt_a < 0 or cnt_b < 0:
        return False
    n = len(x)
    for i in range(n):
        if x[i] != "C":
            continue
        if cnt_a:
            x[i] = "A"
            cnt_a -= 1
        elif cnt_b:
            x[i] = "B"
            cnt_b -= 1

    que = deque()
    for i in range(n):
        if x[i] == "B":
            que.append(i)
    for i in range(n):
        if x[i] == "B":
            que.popleft()
            if y[i] == "B":
                continue
            else:
                return False
        else:
            if y[i] == "A":
                continue
            else:
                j = que.popleft()
                x[i] = "B"
                x[j] = "A"
    return True


def check_case():
    N, X, Y = input().split()
    N = int(N) + 1
    X = list(X) + ["C"]
    Y = list(Y) + ["C"]
    prev = -1
    xs = []
    ys = []

    for i in range(N):
        if Y[i] != "C":
            continue
        if Y[i] == "C" and X[i] != "C":
            return False
        if prev + 1 < i:
            xs.append(X[prev + 1 : i])
            ys.append(Y[prev + 1 : i])
        prev = i

    for x, y in zip(xs, ys):
        if check(x, y):
            continue
        return False
    return True


for _ in range(T):
    print("Yes" if check_case() else "No")
