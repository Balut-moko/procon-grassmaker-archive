from heapq import heappop, heappush


H, W = map(int, input().split())
grid = [input() for _ in [0] * H]

N = int(input())
Medicines = dict()
for _ in range(N):
    R, C, E = map(int, input().split())
    R -= 1
    C -= 1
    Medicines[(R, C)] = E


for r in range(H):
    for c in range(W):
        if grid[r][c] == "S":
            sr, sc = r, c
        if grid[r][c] == "T":
            tr, tc = r, c


dist = [[-1] * W for _ in range(H)]
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
d = Medicines.get((sr, sc), 0)
hq = [(-d, sr, sc)]
dist[sr][sc] = d

while hq:
    d, r, c = heappop(hq)
    d *= -1
    if d < dist[r][c]:
        continue
    if d == 0:
        continue
    for dr, dc in dd:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < H and 0 <= nc < W) or grid[nr][nc] == "#":
            continue
        nd = max(d - 1, Medicines.get((nr, nc), 0))
        if dist[nr][nc] < nd:
            dist[nr][nc] = nd
            heappush(hq, (-dist[nr][nc], nr, nc))

print("Yes" if dist[tr][tc] >= 0 else "No")
