from sys import stdin

readline = stdin.readline
n = int(readline())
r = readline()[:-1]
ans = 0
for s in r:
    if s != 'F':
        ans += 69 - ord(s)
print(ans / n)
