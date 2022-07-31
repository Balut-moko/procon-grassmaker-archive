from sys import stdin

readline = stdin.readline
y = int(readline())
mod = y % 4

if mod == 0:
    ans = y + 2
if mod == 1:
    ans = y + 1
if mod == 2:
    ans = y
if mod == 3:
    ans = y + 3
print(ans)
