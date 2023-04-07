from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

cumsum = [0]

for i in range(n):
    e = 0
    if s[i] == "E":
        e = 1
    cumsum.append(cumsum[i] + e)

ans = 1 << 60
for i in range(n):
    l = i - cumsum[i]
    r = cumsum[n] - cumsum[i + 1]
    ans = min(ans, l + r)

print(ans)
