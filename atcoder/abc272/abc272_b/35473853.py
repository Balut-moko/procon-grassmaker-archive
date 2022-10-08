from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

dp = [[0] * n for _ in [0] * n]

for i in range(m):
    k, *x = map(lambda x: int(x) - 1, readline().split())
    for a in x:
        for b in x:
            if a == b:
                continue
            dp[a][b] = 1
            dp[b][a] = 1

for i in range(n):
    for j in range(i + 1, n):
        if dp[i][j] == 1:
            continue
        print("No")
        exit()
print("Yes")
