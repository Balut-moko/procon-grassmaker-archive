A, B = map(int, input().split())
ans = 0
for i in range(-200, 200):
    li = [A, B, i]
    li.sort()

    if li[1] - li[0] == li[2] - li[1]:
        ans += 1

print(ans)
