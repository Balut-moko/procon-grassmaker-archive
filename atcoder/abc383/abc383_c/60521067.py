from heapq import heappop, heappush


def grid_dijkstra(start_lst):
    hq = []
    for sr, sc in start_lst:
        dist[sr][sc] = 0
        hq.append((0, sr, sc))

    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    while hq:
        d, r, c = heappop(hq)
        if dist[r][c] < d:
            continue
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < H and 0 <= nc < W) or S[nr][nc] == "#":
                continue
            if dist[nr][nc] > d + 1:
                dist[nr][nc] = d + 1
                heappush(hq, (dist[nr][nc], nr, nc))


H, W, D = map(int, input().split())
S = [input() for _ in [0] * H]

start_lst = []
for r in range(H):
    for c in range(W):
        if S[r][c] == "H":
            start_lst.append((r, c))

dist = [[1 << 60] * W for _ in range(H)]

grid_dijkstra(start_lst)

ans = 0
for xr in range(H):
    for xc in range(W):
        if S[xr][xc] == "#":
            continue
        if dist[xr][xc] > D:
            continue
        ans += 1

print(ans)
