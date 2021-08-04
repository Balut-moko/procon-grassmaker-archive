from sys import stdin

readline = stdin.readline
s = readline()[:-1]
cnt = 0
ans = 0
for val in s:
    if val == 'B':
        cnt += 1
    else:
        ans += cnt
print(ans)
