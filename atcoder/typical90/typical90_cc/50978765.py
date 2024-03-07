N, K = map(int, input().split())

grid = [[0] * 5001 for _ in range(5001)]
for _ in range(N):
    A, B = map(int, input().split())
    grid[A][B] += 1

for i in range(5001):
    for j in range(1, 5001):
        grid[i][j] += grid[i][j - 1]

for i in range(1, 5001):
    for j in range(5001):
        grid[i][j] += grid[i - 1][j]

ans = 0
for a in range(1, 5001):
    for b in range(1, 5001):
        tmp = grid[min(a + K, 5000)][min(b + K, 5000)]
        tmp -= grid[a - 1][min(b + K, 5000)]
        tmp -= grid[min(a + K, 5000)][b - 1]
        tmp += grid[a - 1][b - 1]
        ans = max(ans, tmp)

print(ans)
