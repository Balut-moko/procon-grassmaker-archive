from sys import stdin

readline = stdin.readline
a, b, c = readline()[:-1]

ans = 111 * (int(a) + int(b) + int(c))
print(ans)
