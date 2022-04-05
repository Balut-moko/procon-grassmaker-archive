from sys import stdin

readline = stdin.readline
a, b, x = map(int, readline().split())

div_a, mod_a = divmod(a, x)
div_b, mod_b = divmod(b, x)
if div_a == div_b:
    ans = 0
else:
    ans = div_b - div_a
if mod_a == 0:
    ans += 1
print(ans)
