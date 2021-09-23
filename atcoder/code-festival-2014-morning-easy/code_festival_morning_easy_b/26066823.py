from sys import stdin

readline = stdin.readline
n = int(readline())
div, mod = divmod(n, 20)
if mod == 0:
    div -= 1
    mod = 20
if div % 2 == 0:
    ans = mod
else:
    ans = 21 - mod
print(ans)
