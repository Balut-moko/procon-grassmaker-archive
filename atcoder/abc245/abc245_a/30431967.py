from sys import stdin

readline = stdin.readline
a, b, c, d = map(int, readline().split())
if a < c:
    ans = "Takahashi"
elif a > c:
    ans = "Aoki"
else:
    if b <= d:
        ans = "Takahashi"
    else:
        ans = "Aoki"

print(ans)
