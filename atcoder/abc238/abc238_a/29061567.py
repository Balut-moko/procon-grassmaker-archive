from sys import stdin

readline = stdin.readline
n = int(readline())
if 2 ** n > n * n:
    ans = "Yes"
else:
    ans = "No"
print(ans)
