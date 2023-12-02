N, S, M, L = map(int, input().split())
ans = 1 << 60
for i in range(20):
    for j in range(20):
        for k in range(20):
            if i * 6 + j * 8 + 12 * k >= N:
                cost = S * i + M * j + L * k
                ans = min(ans, cost)

print(ans)
