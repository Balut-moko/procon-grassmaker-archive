N = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))
S = input()

MOD = 998244353

ans = [1, 1]
used = [False] * N
for p in P:
    if used[(p + 1) % N]:
        if S[p] == "?":
            ans[0] *= 2
    else:
        if S[p] == "R":
            ans[0] *= 0
    ans[0] %= MOD
    if used[(p - 1) % N]:
        if S[p] == "?":
            ans[1] *= 2
    else:
        if S[p] == "L":
            ans[1] *= 0
    ans[1] %= MOD
    used[p] = True

print(sum(ans) % MOD)
