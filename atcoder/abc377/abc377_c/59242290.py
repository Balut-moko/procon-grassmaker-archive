N, M = map(int, input().split())
dd = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
avoid = set()
for _ in range(M):
    a, b = map(int, input().split())
    avoid.add((a, b))
    for dr, dc in dd:
        if not (1 <= a + dr <= N):
            continue
        if not (1 <= b + dc <= N):
            continue
        avoid.add((a + dr, b + dc))

print(N * N - len(avoid))
