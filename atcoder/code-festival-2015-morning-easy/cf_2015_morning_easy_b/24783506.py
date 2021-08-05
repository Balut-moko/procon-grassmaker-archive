from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
if n % 2 == 1:
    ans = -1
else:
    ans = 0
    for i in range(n // 2):
        if s[i] != s[i + n // 2]:
            ans += 1
print(ans)
