from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]
ab.sort()


money_set = set()
money_set.add(0)
for i in range(n):
    tmp = money_set.copy()
    for val in tmp:
        for j in range(1, ab[i][1] + 1):
            if val + ab[i][0] * j <= x:
                money_set.add(val + ab[i][0] * j)

print("Yes" if x in money_set else "No")
