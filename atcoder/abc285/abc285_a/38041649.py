from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())

print("Yes" if a == b // 2 else "No")
