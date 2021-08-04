from sys import stdin

readline = stdin.readline
s = readline()[:-1]
k = int(readline())
ans = 1
for i in range(len(s)):
    if s[i] != '1' or k == i + 1:
        ans = s[i]
        break

print(ans)
