N = int(input())
AB = [tuple(map(int, input().split())) for _ in [0] * N]
ans = 0
mx = 0
for a, b in AB:
    ans += a
    mx = max(mx, b - a)

print(ans + mx)
