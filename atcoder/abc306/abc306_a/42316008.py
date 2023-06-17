from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

ans = ""
for val in s:
    ans += val + val

print(ans)
