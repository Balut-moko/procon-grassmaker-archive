from sys import stdin

readline = stdin.readline
s = readline()[:-1]
tmp = s[0]
cnt = 0
ans = ''

for i in range(len(s)):
    if tmp == s[i]:
        cnt += 1
    else:
        ans += tmp + str(cnt)
        tmp = s[i]
        cnt = 1
ans += tmp + str(cnt)
print(ans)
