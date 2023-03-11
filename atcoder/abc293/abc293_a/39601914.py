from sys import stdin

readline = stdin.readline
s = readline()[:-1]

ans = ""

for i in range(len(s) // 2):
    ans += s[2 * i+1] + s[2 * i]
print(ans)
