from sys import stdin

readline = stdin.readline
n = int(readline())
coins = list(map(int, readline().split()))
coins.sort()
ans = 10000
for c in range(10000):
    for b in range(10000 - c):
        if (n - c * coins[2] - b * coins[1]) % coins[0] == 0:
            a = (n - c * coins[2] - b * coins[1]) // coins[0]
            if a >= 0:
                ans = min(ans, a + b + c)

print(ans)
