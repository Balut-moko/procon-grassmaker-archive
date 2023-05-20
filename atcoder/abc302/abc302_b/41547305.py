from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * h]
dd = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1))
sn = "snuke"
for r in range(h):
    for c in range(w):
        if s[r][c] == "s":
            for dr, dc in dd:
                ans = [(r + 1, c + 1)]
                nr = r
                nc = c
                for k in range(1, 5):
                    nr = nr + dr
                    nc = nc + dc
                    if not (0 <= nr < h and 0 <= nc < w):
                        break
                    if s[nr][nc] != sn[k]:
                        break
                    ans.append((nr + 1, nc + 1))
                else:
                    for val in ans:
                        print(*val)
                    exit()
