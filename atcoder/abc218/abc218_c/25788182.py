from sys import stdin

readline = stdin.readline
n = int(readline())
s = [list(readline()[:-1]) for _ in [0] * n]
t = [list(readline()[:-1]) for _ in [0] * n]
cnt_s = sum(1 for i in range(n) for j in range(n) if s[i][j] == '#')
cnt_t = sum(1 for i in range(n) for j in range(n) if t[i][j] == '#')
if cnt_s != cnt_t:
    print('No')
    exit()
ans = 'No'
for i in range(n):
    for j in range(n):
        if t[i][j] == '#':
            ti, tj = i, j
            break
    else:
        continue
    break

for _ in range(4):
    s = [list(x)[::-1] for x in zip(*s)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                si, sj = i, j
                break
        else:
            continue
        break
    for i in range(n):
        for j in range(n):
            ii = i + ti - si
            jj = j + tj - sj
            if 0 <= ii < n and 0 <= jj < n:
                if s[i][j] != t[ii][jj]:
                    break
            else:
                if s[i][j] == '#':
                    break
        else:
            continue
        break
    else:
        ans = 'Yes'

print(ans)
