from sys import stdin

readline = stdin.readline
s = readline()[:-1]
ans = 100
for i in range(26):
    al = chr(ord("a") + i)
    cnt = 0
    ss = s
    while ss != al * len(ss):
        tmp = ""
        for i in range(len(ss) - 1):
            if ss[i] == al or ss[i + 1] == al:
                tmp += al
            else:
                tmp += ss[i]
        ss = tmp
        cnt += 1
    ans = min(ans, cnt)
print(ans)
