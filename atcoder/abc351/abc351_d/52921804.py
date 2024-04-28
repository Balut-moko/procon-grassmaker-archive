from collections import deque


def bfs(sr, sc):
    h = len(S)
    w = len(S[0])
    cnt = 1
    used[sr][sc] = True
    mug_set = set()
    que = deque([(sr, sc)])
    while que:
        r, c = que.popleft()
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w) or S[nr][nc] == "#":
                continue
            if S[nr][nc] == "m":
                if (nr, nc) not in mug_set:
                    cnt += 1
                mug_set.add((nr, nc))
                continue
            if not used[nr][nc]:
                cnt += 1
                used[nr][nc] = True
                que.append((nr, nc))
    return cnt


H, W = map(int, input().split())
S = [list(input()) for _ in [0] * H]
used = [[False] * W for _ in range(H)]
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

for r in range(H):
    for c in range(W):
        if S[r][c] != "#":
            continue
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            if S[nr][nc] == ".":
                S[nr][nc] = "m"

ans = 0
for r in range(H):
    for c in range(W):
        if S[r][c] == "#":
            continue
        if S[r][c] == "m":
            ans = max(ans, 1)
            continue
        ans = max(ans, bfs(r, c))

print(ans)
