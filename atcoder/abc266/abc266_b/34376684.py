from sys import stdin

readline = stdin.readline
n = int(readline())

div, mod = divmod(n, 998244353)
print(mod)
