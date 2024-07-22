from collections import deque


H, W, Y = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in [0] * H]
M = 100010

ans = H * W
sunk = [[False] * W for _ in range(H)]

que = [deque() for i in range(M)]

for r in range(H):
    for c in range(W):
        if r in [0, H - 1] or c in [0, W - 1]:
            que[A[r][c]].append((r, c))

dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

for y in range(1, Y + 1):
    while que[y]:
        r, c = que[y].popleft()
        if sunk[r][c]:
            continue
        ans -= 1
        sunk[r][c] = True
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            que[max(y, A[nr][nc])].append((nr, nc))
    print(ans)
