from sys import stdin

readline = stdin.readline
s = readline()[:-1]
t = readline()[:-1]

if len(t) < len(s):
    print("No")
    exit()
ans = "Yes"
for i in range(len(s)):
    if s[i] != t[i]:
        ans = "No"
print(ans)
