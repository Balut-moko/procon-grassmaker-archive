from sys import stdin

readline = stdin.readline
s = list(readline()[:-1])
t = list(readline()[:-1])
ans_li = []
for i in range(len(s)):
    if i + len(t) <= len(s):
        tmp = s.copy()
        for j in range(len(t)):
            if tmp[i + j] == t[j]:
                continue
            if tmp[i + j] == '?':
                tmp[i + j] = t[j]
                continue
            break
        else:
            tmp = [val if val != '?' else 'a' for val in tmp]
            ans_li.append(tmp)
if ans_li:
    ans_li.sort()
    print(*ans_li[0], sep="")
else:
    print('UNRESTORABLE')
