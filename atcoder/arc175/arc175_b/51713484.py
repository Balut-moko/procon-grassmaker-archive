def check(s):
    mn = 0
    cnt = 0
    for c in s:
        if c == "(":
            cnt += 1
        else:
            cnt -= 1
        mn = min(mn, cnt)
    return mn, cnt


N, A, B = map(int, input().split())
S = list(input())
_, cnt = check(S)
ans = abs(cnt) // 2 * B
if cnt < 0:
    idx = 0
    while cnt != 0:
        if S[idx] == ")":
            S[idx] = "("
            cnt += 2
        idx += 1
else:
    idx = 2 * N - 1
    while cnt != 0:
        if S[idx] == "(":
            S[idx] = ")"
            cnt -= 2
        idx -= 1

mn, _ = check(S)
ans += (-mn + 1) // 2 * min(A, B * 2)
print(ans)
