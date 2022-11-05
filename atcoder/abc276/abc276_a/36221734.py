from sys import stdin

readline = stdin.readline
s = readline()[:-1]
ans = -1
for i in range(len(s)):
    if s[i] == "a":
        ans = i + 1

print(ans)
