from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
for i in range(256):
    if a ^ i == b:
        ans = i
print(ans)
