from heapq import heappop, heappush


def grid_dijkstra(sr, sc):
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    hq = []
    seen = [[False] * W for _ in range(H)]
    seen[sr][sc] = True
    for dr, dc in dd:
        nr = sr + dr
        nc = sc + dc
        if not (0 <= nr < H and 0 <= nc < W):
            continue
        heappush(hq, (S[nr][nc], nr, nc))
        seen[nr][nc] = True
    res = S[sr][sc]
    while hq:
        s, r, c = heappop(hq)
        if res <= s * X:
            break
        res += s
        seen[r][c] = True
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < H and 0 <= nc < W) or seen[nr][nc]:
                continue
            heappush(hq, (S[nr][nc], nr, nc))
            seen[nr][nc] = True
    return res


H, W, X = map(int, input().split())
P, Q = map(lambda x: int(x) - 1, input().split())

S = [tuple(map(int, input().split())) for _ in [0] * H]

print(grid_dijkstra(P, Q))
