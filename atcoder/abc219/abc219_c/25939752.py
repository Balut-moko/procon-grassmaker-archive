from sys import stdin


def rename(name, x):
    res = ''
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for s in name:
        idx = x.index(s)
        res += abc[idx]
    return res


readline = stdin.readline
x = readline()[:-1]
n = int(readline())
s = [readline()[:-1] for _ in [0] * n]
ans = []
for name in s:
    re = rename(name, x)
    ans.append([re, name])
ans.sort()
for a in ans:
    print(a[1])
