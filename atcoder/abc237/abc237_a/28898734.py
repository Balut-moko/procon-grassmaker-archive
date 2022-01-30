from sys import stdin

readline = stdin.readline
n = int(readline())
if -(2 ** 31) <= n < 2 ** 31:
    ans = "Yes"
else:
    ans = "No"
print(ans)
