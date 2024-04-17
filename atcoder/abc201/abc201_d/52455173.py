import pypyjit
import sys

pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10**7)


def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    # 終端条件
    if i == H - 1 and j == W - 1:
        return 0
    # 打てる手をすべて試す
    res = -1 << 60
    if i + 1 < H:
        p = 1 if A[i + 1][j] == "+" else -1
        res = max(res, -dfs(i + 1, j) + p)
    if j + 1 < W:
        p = 1 if A[i][j + 1] == "+" else -1
        res = max(res, -dfs(i, j + 1) + p)

    dp[i][j] = res
    return res


H, W = map(int, input().split())
A = [input() for _ in range(H)]

dp = [[-1] * W for _ in [0] * H]

res = dfs(0, 0)

if res > 0:
    print("Takahashi")
elif res < 0:
    print("Aoki")
else:
    print("Draw")
