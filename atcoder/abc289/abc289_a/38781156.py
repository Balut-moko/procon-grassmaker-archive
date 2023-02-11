from sys import stdin

readline = stdin.readline
s = readline()[:-1]
ans = ""
for val in s:
    if val == "0":
        ans += "1"
    else:
        ans += "0"
print(ans)
