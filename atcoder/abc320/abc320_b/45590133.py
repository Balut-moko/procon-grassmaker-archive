s = input()

ans = 0
n = len(s)
for i in range(n):
    for j in range(i, n + 1):
        t = s[i:j]
        if t == t[::-1]:
            ans = max(ans, len(t))
print(ans)
