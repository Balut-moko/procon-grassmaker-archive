from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))
ans = []

for i in range(n):
    for j in range(n - 2):
        if p[j] % 2 != p[j + 2] % 2 and p[j] % 2 != j % 2:
            p[j + 2], p[j] = p[j], p[j + 2]
            ans.append(["B", j + 1])
for i in range(n - 1):
    if p[i] % 2 != p[i + 1] and p[i] % 2 == i % 2:
        p[i + 1], p[i] = p[i], p[i + 1]
        ans.append(["A", i + 1])
for i in range(n):
    for j in range(n - 2):
        if p[j] > p[j + 2]:
            p[j + 2], p[j] = p[j], p[j + 2]
            ans.append(["B", j + 1])
print(len(ans))
for val in ans:
    print(*val)
