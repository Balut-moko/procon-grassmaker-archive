from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * h]
nxt = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 'Yes'
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            for a, b in nxt:
                nxt_i, nxt_j = i + a, j + b
                if 0 <= nxt_i < h and 0 <= nxt_j < w:
                    if s[nxt_i][nxt_j] == '#':
                        break
            else:
                ans = 'No'
                break
    else:
        continue
    break
print(ans)
