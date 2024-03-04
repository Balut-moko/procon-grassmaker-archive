N = int(input())
A = list(map(int, input().split()))

dp = [[0] * 200 for _ in [0] * N]
dp[0][0] = 1
dp[0][A[0] % 200] += 1
for i in range(1, N):
    for j in range(200):
        dp[i][j] += dp[i - 1][j]
        dp[i][(j + A[i]) % 200] += dp[i - 1][j]


def restore(m):
    mb = m
    B = []
    for i in range(N - 1, 0, -1):
        if dp[i - 1][mb] > 0:
            continue
        B.append(i + 1)
        mb = (mb - A[i] + 200) % 200
    if mb != 0 or A[0] == 200:
        B.append(1)
    C = []
    for i in range(N - 1, 0, -1):
        if dp[i - 1][(m - A[i] + 200) % 200] > 0:
            C.append(i + 1)
            m = (m - A[i] + 200) % 200
    if m != 0:
        C.append(1)

    return B[::-1], C[::-1]


for j in range(200):
    if dp[-1][j] >= 2:
        m = j
        B, C = restore(m)
        if min(len(B), len(C)) != 0 and B != C:
            print("Yes")
            print(len(B), *B)
            print(len(C), *C)
            exit()

print("No")
