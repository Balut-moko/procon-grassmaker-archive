from collections import defaultdict

N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0] * 2000 for _ in [0] * 52]
for i in range(52):
    for j in range(1400):
        if i == 0 and j <= 1:
            continue
        s = defaultdict(int)
        if i >= 1:
            s[dp[i - 1][i + j]] = 1
        if j >= 2:
            for k in range(1, j // 2 + 1):
                s[dp[i][j - k]] = 1
        g = 0
        while s[g] != 0:
            g += 1
        dp[i][j] = g

ans = 0
for w, b in zip(W, B):
    ans ^= dp[w][b]
print("First" if ans > 0 else "Second")
