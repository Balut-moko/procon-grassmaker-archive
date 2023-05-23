from sys import stdin

readline = stdin.readline
n = int(readline())
s1 = readline()[:-1]
s2 = readline()[:-1]
s = [s1, s2]

if s[0][0] == s[1][0]:
    ans = 3
    pre = 0
else:
    ans = 6
    pre = 1
mod = 10**9 + 7

for i in range(1, n):
    if s[0][i - 1] == s[0][i]:
        continue
    if s[0][i] == s[1][i]:
        if pre == -1:
            ans = 3
        elif pre == 0:
            ans *= 2
            ans %= mod
        pre = 0
    else:
        if pre == -1:
            ans = 6
        elif pre == 0:
            ans *= 2
            ans %= mod
        else:
            ans *= 3
            ans %= mod
        pre = 1
print(ans)