from sys import stdin

readline = stdin.readline
s = readline()[:-1]
keyence = 'keyence'
cnt = 0
for i in range(7):
    if keyence[i] == s[i]:
        cnt += 1
    else:
        break
for i in range(7):
    if keyence[6 - i] == s[len(s) - i - 1]:
        cnt += 1
    else:
        break

if cnt < 7:
    ans = 'NO'
else:
    ans = 'YES'
print(ans)
