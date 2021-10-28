from sys import stdin

readline = stdin.readline
n = int(readline())
s = list(readline()[:-1])
ans = 0
for i in range(n):
    a = s[:i]
    b = s[i:]
    a_s = set(a)
    b_s = set(b)
    tmp = a_s & b_s
    ans = max(ans, len(tmp))
print(ans)
