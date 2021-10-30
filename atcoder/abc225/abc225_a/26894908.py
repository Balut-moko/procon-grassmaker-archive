from sys import stdin

readline = stdin.readline
s = readline()[:-1]
if s[0] == s[1] and s[0] == s[2]:
    ans = 1
elif s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
    ans = 3
else:
    ans = 6
print(ans)
