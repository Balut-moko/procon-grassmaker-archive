N, S = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in [0] * N]

dp = [[False] * (S + 1) for _ in [0] * (N + 1)]
dp[0][0] = True
for i in range(1, N + 1):
    A, B = AB[i - 1]
    for s in range(S + 1):
        if s - A >= 0:
            if dp[i - 1][s - A]:
                dp[i][s] = True
        if s - B >= 0:
            if dp[i - 1][s - B]:
                dp[i][s] = True

if not dp[N][S]:
    print("Impossible")
    exit()

ans = ["B"] * N
for i in range(N, 0, -1):
    A, B = AB[i - 1]
    if S - A >= 0:
        if dp[i - 1][S - A]:
            ans[i - 1] = "A"
            S -= A
        else:
            S -= B
    else:
        S -= B
print("".join(ans))
