from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())

ans = [["N"] * n for _ in [0] * n]

for _ in range(q):
    que = list(map(int, readline().split()))
    a = que[1] - 1

    if que[0] == 1:
        b = que[2] - 1
        ans[a][b] = "Y"
    elif que[0] == 2:
        for j in range(n):
            if a == j:
                continue
            if ans[j][a] == "Y":
                ans[a][j] = "Y"
    else:
        f = []
        for x in range(n):
            if a == x:
                continue
            if ans[a][x] == "Y":
                f.append(x)
        for j in f:
            for i in range(n):
                if a == i:
                    continue
                if ans[j][i] == "Y":
                    ans[a][i] = "Y"

for val in ans:
    print(*val, sep="")
