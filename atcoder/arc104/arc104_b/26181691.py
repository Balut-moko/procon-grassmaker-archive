from sys import stdin

readline = stdin.readline
n, s = readline().split()
n = int(n)
ans = 0
for i in range(n):
    cnt1, cnt2 = 0, 0
    for j in range(i, n):
        if s[j] == 'A':
            cnt1 += 1
        if s[j] == 'T':
            cnt1 -= 1
        if s[j] == 'C':
            cnt2 += 1
        if s[j] == 'G':
            cnt2 -= 1
        if cnt1 == 0 and cnt2 == 0:
            ans += 1
print(ans)
