from atcoder.dsu import DSU


H, W = map(int, input().split())
S = [input() for _ in [0] * H]

uf = DSU(H * W)
cnt = 0
for h in range(H):
    for w in range(W):
        if S[h][w] != "#":
            cnt += 1
            continue
        dd = ((-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
        for dx, dy in dd:
            if 0 <= h + dx < H and 0 <= w + dy < W:
                if S[h + dx][w + dy] == "#":
                    uf.merge(h * W + w, (h + dx) * W + w + dy)


print(len(uf.groups()) - cnt)
