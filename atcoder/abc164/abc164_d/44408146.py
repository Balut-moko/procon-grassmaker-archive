from sys import stdin

readline = stdin.readline
s = readline()[:-1]
n = len(s)

ans = 0
cnt = [0] * 2020

cnt[0] = 1
tmp = 0
p = 1

for i in range(n - 1, -1, -1):
    tmp = (tmp + (ord(s[i]) - ord("0")) * p) % 2019
    ans += cnt[tmp]
    p = (p * 10) % 2019
    cnt[tmp] += 1
print(ans)
