from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
m = int(readline())
b = set(map(int, readline().split()))
x = int(readline())

dp = [False] * (x + 1)

dp[0] = True

for i in range(x + 1):
    if dp[i]:
        for val in a:
            if (i + val) <= x and (i + val) not in b:
                dp[i + val] = True
print("Yes" if dp[x] else "No")
