from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))

ans = []

for i in range(2, 2 * n):
    if i % 2 == 0:
        if p[i - 2] < p[i - 1]:
            if p[i - 1] < p[i]:
                p[i - 1], p[i] = p[i], p[i - 1]
                ans.append(i)
        else:
            if p[i - 1] > p[i]:
                p[i - 1], p[i - 2] = p[i - 2], p[i - 1]
                ans.append(i - 1)
            else:
                if p[i - 2] < p[i]:
                    p[i - 1], p[i] = p[i], p[i - 1]
                    ans.append(i)
                else:
                    p[i - 1], p[i - 2] = p[i - 2], p[i - 1]
                    ans.append(i - 1)

if p[2 * n - 2] > p[2 * n - 1]:
    ans.append(2 * n - 1)

print(len(ans))
print(*ans)
