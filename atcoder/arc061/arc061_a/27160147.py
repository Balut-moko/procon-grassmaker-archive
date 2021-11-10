from sys import stdin

readline = stdin.readline
s = readline()[:-1]
ans = 0
for i in range(2**(len(s) - 1)):
    tmp = s[0]
    for j in range(len(s) - 1):
        if ((i >> j) & 1):
            tmp += '+' + s[j + 1]
        else:
            tmp += s[j + 1]
    ans += eval(tmp)
print(ans)
