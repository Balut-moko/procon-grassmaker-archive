from sys import stdin

readline = stdin.readline
n = int(readline())
if n % 2 == 1:
    exit(print())
ans = []
for i in range(1 << n):
    cnt = 0
    for j in range(n):
        if (i >> j) & 1 == 1:
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        tmp = ""
        for j in range(n):
            if (i >> j) & 1 == 1:
                tmp += "("
            else:
                tmp += ")"
        ans.append(tmp)
ans.sort()
for v in ans:
    print(v)
