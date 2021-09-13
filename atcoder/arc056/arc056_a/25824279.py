from sys import stdin

readline = stdin.readline
a, b, k, l = map(int, readline().split())

div, mod = divmod(k, l)
ans = min((div + 1) * b, div * b + a * mod)

print(ans)
