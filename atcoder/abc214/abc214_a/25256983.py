from sys import stdin

readline = stdin.readline
n = int(readline())
if n <= 125:
    ans = 4
elif 125 < n <= 211:
    ans = 6
else:
    ans = 8
print(ans)