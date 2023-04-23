from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
s = readline()[:-1]

c = [[n] * 26 for _ in range(n + 1)]
for i in reversed(range(n)):
    for j in range(26):
        if ord(s[i]) - ord("a") == j:
            c[i][j] = i
        else:
            c[i][j] = c[i + 1][j]
ans = []
now = 0
for i in range(k):
    for j in range(26):
        pos = c[now][j]
        if k <= n - pos + i:
            ans.append(chr(ord("a") + j))
            now = pos + 1
            break

print(*ans, sep="")
