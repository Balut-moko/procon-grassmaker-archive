N = int(input())

dame = N
if N % 2 == 1:
    dame -= 1
ans = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j <= i:
            continue
        if j == dame:
            continue
        ans.append((i, j))
    dame -= 1

print(len(ans))
for v in ans:
    print(*v)
