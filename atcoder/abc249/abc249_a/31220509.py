from sys import stdin

readline = stdin.readline
a, b, c, d, e, f, x = map(int, readline().split())
div, mod = divmod(x, a + c)
takahashi = div * a * b + min(a, mod) * b
div, mod = divmod(x, d + f)
aoki = div * d * e + min(d, mod) * e
if takahashi == aoki:
    ans = "Draw"
elif takahashi > aoki:
    ans = "Takahashi"
else:
    ans = "Aoki"
print(ans)
