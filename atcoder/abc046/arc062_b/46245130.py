S = input()

ans = 0
cnt = 1
g_cnt = S.count("g")
if S[0] == "p":
    ans -= 1
else:
    g_cnt -= 1

for val in S[1:]:
    if val == "g":
        if g_cnt <= cnt:
            ans += 1
            cnt -= 1
        else:
            cnt += 1
        g_cnt -= 1
    else:
        if 0 < cnt:
            cnt -= 1
        else:
            ans -= 1
            cnt += 1
print(ans)
