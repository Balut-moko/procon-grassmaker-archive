from sys import stdin

readline = stdin.readline
s = readline()[:-1]

ans = 0
for i, val in enumerate(s[::-1]):
    ans += (ord(val) - ord("A") + 1) * (26 ** i)
print(ans)
