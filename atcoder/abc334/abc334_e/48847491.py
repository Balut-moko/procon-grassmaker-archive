from atcoder.dsu import DSU


H, W = map(int, input().split())
S = [list(input()) for _ in [0] * H]
MOD = 998244353
uf = DSU(H * W)
Rcnt = 0

for r in range(H):
    for c in range(W):
        if S[r][c] == ".":
            Rcnt += 1
            continue
        dd = ((0, 1), (1, 0))
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < H and 0 <= nc < W) or S[nr][nc] == ".":
                continue
            uf.merge(r * W + c, nr * W + nc)

cnt = 0
total = len(uf.groups()) - Rcnt
for r in range(H):
    for c in range(W):
        if S[r][c] == "#":
            continue
        dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
        tmp = set()
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < H and 0 <= nc < W) or S[nr][nc] == ".":
                continue
            tmp.add(uf.leader(nr * W + nc))
        cnt += total - len(tmp) + 1

inv = pow(Rcnt, -1, MOD)
print(cnt * inv % MOD)
