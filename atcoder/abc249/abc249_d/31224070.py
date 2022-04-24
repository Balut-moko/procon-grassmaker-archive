from sys import stdin


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
c = [0] * 200001

for val in a:
    c[val] += 1

ans = 0
for i in range(1, 200001):
    for j in range(1, 200001):
        if i * j >= 200001:
            break
        ans += c[i] * c[j] * c[i * j]

print(ans)
