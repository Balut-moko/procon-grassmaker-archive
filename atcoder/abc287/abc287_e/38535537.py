from sys import stdin


def lcp(s, t):
    res = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            res += 1
        else:
            break
    return res


readline = stdin.readline
n = int(readline())
s = [readline()[:-1] for _ in [0] * n]
si = []
for i, val in enumerate(s):
    si.append((val, i))
si.sort()

ans = [0] * n

for i in range(n):
    tmp1 = lcp(si[i][0], si[(i + 1) % n][0])
    tmp2 = lcp(si[i - 1][0], si[i][0])
    ans[si[i][1]] = max(tmp1, tmp2)
print(*ans, sep="\n")
