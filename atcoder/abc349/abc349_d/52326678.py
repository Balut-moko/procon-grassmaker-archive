L, R = map(int, input().split())

l = L
ans = []
while l != R:
    i = 60
    while True:
        j = l // 2**i
        if 2**i * j == l and 2**i * (j + 1) <= R:
            ans.append((2**i * j, 2**i * (j + 1)))
            break
        i -= 1
    l = 2**i * (j + 1)


print(len(ans))
for val in ans:
    print(*val)
