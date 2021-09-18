from sys import stdin

readline = stdin.readline
x = int(readline())
if 90 <= x:
    ans = 'expert'
elif 70 <= x < 90:
    ans = 90 - x
elif 40 <= x < 70:
    ans = 70 - x
else:
    ans = 40 - x
print(ans)
