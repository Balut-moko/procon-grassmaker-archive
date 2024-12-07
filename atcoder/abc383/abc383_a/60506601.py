N = int(input())
TV = [list(map(int, input().split())) for _ in range(N)]
ans = 0
idx = 0
for i in range(1, TV[-1][0] + 1):
    ans = max(ans - 1, 0)
    if TV[idx][0] == i:
        ans += TV[idx][1]
        idx += 1
        if idx == TV[-1][0] + 1:
            break

print(ans)
