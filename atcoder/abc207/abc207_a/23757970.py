from sys import stdin

readline = stdin.readline
num = list(map(int, readline().split()))
ans = sum(num) - min(num)

print(ans)
