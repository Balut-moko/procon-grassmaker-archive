from sys import stdin

readline = stdin.readline
s = readline()[:-1]
t = readline()[:-1]
ans = len(t)
for i in range(len(s)):
    if s[i] != t[i]:
        ans = i + 1
        break
print(ans)
