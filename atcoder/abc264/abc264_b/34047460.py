from sys import stdin

readline = stdin.readline
r, c = map(int, readline().split())

if max(abs(r - 8), abs(c - 8)) % 2 == 1:
    ans = "black"
else:
    ans = "white"
print(ans)
