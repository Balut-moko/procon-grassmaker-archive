from sys import stdin

readline = stdin.readline
a, b, c = map(int, readline().split())
if a <= b <= c or c <= b <= a:
    ans = "Yes"
else:
    ans = "No"
print(ans)
