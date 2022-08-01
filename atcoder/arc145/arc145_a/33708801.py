from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

if s == "BA" or (s[0] == "A" and s[-1] == "B"):
    ans = "No"
else:
    ans = "Yes"
print(ans)
