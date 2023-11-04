A = [tuple(map(int, input().split())) for _ in [0] * 9]


def check(A):
    for i in range(9):
        ss = [A[i][j] for j in range(9)]
        for j in range(1, 10):
            if ss.count(j) >= 2:
                return False
    for j in range(9):
        ss = [A[i][j] for i in range(9)]
        for i in range(1, 10):
            if ss.count(i) >= 2:
                return False
    for i in range(3):
        for j in range(3):
            ss = []
            for ii in range(3):
                for jj in range(3):
                    ss.append(A[i * 3 + ii][j * 3 + jj])
            for k in range(1, 10):
                if ss.count(k) >= 2:
                    return False
    return True


print("Yes" if check(A) else "No")
