from sys import stdin

readline = stdin.readline
n = int(readline())
evidences = []
ans = 0
for i in range(n):
    a = int(readline())
    val = [list(map(int, readline().split())) for _ in range(a)]
    evidences.append(val)

for i in range(2 ** n):
    check = [0] * n
    for j in range(n):
        if (i >> j) & 1:
            check[j] = 1
    for j in range(n):
        if check[j] == 1:
            for x, y in evidences[j]:
                x -= 1
                if check[x] != y:
                    break
            else:
                continue
            break
    else:
        ans = max(ans, sum(check))
        continue
print(ans)
